"""Personagem realista a partir da base do MakeHuman.

Usa a malha base, os morphs (targets), o esqueleto padrao (163 ossos) e os pesos de skin
do MakeHuman, mais texturas de pele e proxies (olhos, sobrancelhas, cilios, dentes, cabelo,
biquini). Adiciona ossos de jiggle (peito = ossos breast do MakeHuman renomeados; gluteo novo).

Dados: rode fetch_makehuman_data.sh e aponte MH_TARGETS / MH_DATA (padrao em /tmp/mh).
Rodar: python build_mh_character.py   (modulo bpy)
"""
import bpy, bmesh, json, math, os
import numpy as np
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
MH_TARGETS = os.environ.get("MH_TARGETS", "/tmp/mh/pypi/makehuman/data/targets.npz")
MH_DATA = os.environ.get("MH_DATA", "/tmp/mh/npm/package/public/data")
# texturas em alta (pele 2048px, olhos 1024px) do pacote npm ara3d-data (CC0, derivado do MakeHuman)
ARA_TEX = os.environ.get("ARA_TEX", "/tmp/mh/ara/package/assets/textures")

# ------------------------------------------------------------------ AJUSTES DO CORPO
# 0..1 como no MakeHuman. gender 0 = feminino. age 0.5 = 25 anos.
MACRO = dict(gender=0.0, age=0.5, muscle=0.55, weight=0.48, height=0.52, proportions=0.8,
             race=dict(caucasian=1.0, african=0.0, asian=0.0))
BREAST = dict(cup=0.92, firmness=0.68)     # 0..1 (0.5 = medio)
EXTRA = {                                  # morphs extras: nome -> peso (negativo = lado "decr")
    "buttocks/buttocks-volume": 0.85,
    "hip/hip-scale-horiz": 0.30,
    "measure/measure-waist-circ": -0.35,
    "stomach/stomach-tone": 0.4,
    "bodyshapes/bodyshapes-elvs-fem-neat-hourglass": 0.45,
}
SKIN = "young_caucasian_female/textures/young_lightskinned_female_diffuse.png"   # fallback 512px
SKIN_HD = "skin_young_caucasian_female.jpg"
HAIR = "long01"
EYE_COLOR = "brown"
OUTFIT = ["F_Bikini_01"]                  # roupas (objetos separados, da pra esconder)
OUTFIT_COLOR = (0.03, 0.05, 0.12, 1)      # None = usa a textura original
UNIT = 0.1                                 # MakeHuman usa decimetros

T = np.load(MH_TARGETS)                    # sem allow_pickle
def tdelta(name):
    i = T[f"targets/{name}.index"]; v = T[f"targets/{name}.vector"].astype(np.float64) * 1e-3
    return i, v

def lerp3(x, names):
    """peso de 3 categorias (min, medio, max) a partir de x em 0..1"""
    if x < 0.5: return {names[0]: 1 - x / 0.5, names[1]: x / 0.5}
    return {names[1]: 1 - (x - 0.5) / 0.5, names[2]: (x - 0.5) / 0.5}

def macro_weights(m):
    g = {"female": 1 - m["gender"], "male": m["gender"]}
    a = m["age"]
    if a < 0.1875: ag = {"baby": 1 - a / 0.1875, "child": a / 0.1875}
    elif a < 0.5:  ag = {"child": 1 - (a - 0.1875) / 0.3125, "young": (a - 0.1875) / 0.3125}
    else:          ag = {"young": 1 - (a - 0.5) / 0.5, "old": (a - 0.5) / 0.5}
    mu = lerp3(m["muscle"], ("minmuscle", "averagemuscle", "maxmuscle"))
    we = lerp3(m["weight"], ("minweight", "averageweight", "maxweight"))
    W = {}
    def add(n, w):
        if w > 1e-4: W[n] = W.get(n, 0) + w
    for gn, gw in g.items():
        for an, aw in ag.items():
            for rn, rw in m["race"].items(): add(f"macrodetails/{rn}-{gn}-{an}", rw * gw * aw)
            for mn, mw in mu.items():
                for wn, ww in we.items():
                    base = gw * aw * mw * ww
                    add(f"macrodetails/universal-{gn}-{an}-{mn}-{wn}", base)
                    h = m["height"]
                    if h > 0.5: add(f"macrodetails/height/{gn}-{an}-{mn}-{wn}-maxheight", base * (h - 0.5) * 2)
                    else:       add(f"macrodetails/height/{gn}-{an}-{mn}-{wn}-minheight", base * (0.5 - h) * 2)
                    p = m["proportions"]
                    if p > 0.5: add(f"macrodetails/proportions/{gn}-{an}-{mn}-{wn}-idealproportions", base * (p - 0.5) * 2)
                    else:       add(f"macrodetails/proportions/{gn}-{an}-{mn}-{wn}-uncommonproportions", base * (0.5 - p) * 2)
                    cup = lerp3(BREAST["cup"], ("mincup", "averagecup", "maxcup"))
                    fir = lerp3(BREAST["firmness"], ("minfirmness", "averagefirmness", "maxfirmness"))
                    for cn, cw in cup.items():
                        for fn, fw in fir.items():
                            if cn == "averagecup" and fn == "averagefirmness": continue
                            add(f"breast/{gn}-{an}-{mn}-{wn}-{cn}-{fn}", base * cw * fw)
    for n, w in EXTRA.items():
        if n.startswith("bodyshapes"): add(n, w)
        else: add(f"{n}-{'incr' if w > 0 else 'decr'}", abs(w))
    return W

# ------------------------------------------------------------------ malha base
base = json.load(open(os.path.join(MH_DATA, "models/human_full_size.json")))
co = np.array(base["vertices"], dtype=np.float64).reshape(-1, 3)
co0 = co.copy()
nverts = len(co)
applied = 0
for name, w in macro_weights(MACRO).items():
    key = f"targets/{name}.index"
    if key not in T.files: print("  (sem target)", name); continue
    i, v = tdelta(name)
    if len(i): co[i] += v * w; applied += 1
print("morphs aplicados:", applied)

GROUND = 0.0
def sync_helpers():
    """Os morphs de busto/gluteo nao movem a 'malha auxiliar' (meia-calca, cabelo...) onde as
    roupas sao encaixadas. Cada vertice auxiliar herda a deformacao do vertice do corpo mais proximo."""
    from mathutils import kdtree
    bset = sorted({v for f in parse_faces(base["faces"]) if f[1] in body_mat_idx for v in f[0]})
    kd = kdtree.KDTree(len(bset))
    for j, vi in enumerate(bset): kd.insert(Vector(co0[vi]), j)
    kd.balance()
    isb = np.zeros(nverts, bool); isb[bset] = True
    d = co - co0
    for vi in np.where(~isb)[0]:
        _, j, _ = kd.find(Vector(co0[vi]))
        bd = d[bset[j]]
        if np.linalg.norm(bd) > np.linalg.norm(d[vi]): co[vi] = co0[vi] + bd

def mh2bl(c):   # MakeHuman (Y cima, frente +Z, dm) -> Blender (Z cima, frente -Y, m), pes no z=0
    return np.stack([c[:, 0], -c[:, 2], c[:, 1]], axis=1) * UNIT - np.array([0, 0, GROUND])

def parse_faces(F, nlayers=1):
    """Formato JSON 3 do three.js -> lista de (verts, material, uv_idx)"""
    out, i = [], 0
    while i < len(F):
        t = F[i]; i += 1
        nv = 4 if t & 1 else 3
        vs = F[i:i + nv]; i += nv
        mat = 0
        if t & 2: mat = F[i]; i += 1
        if t & 4: i += nlayers
        uv = None
        if t & 8: uv = F[i:i + nv]; i += nv * nlayers
        if t & 16: i += 1
        if t & 32: i += nv
        if t & 64: i += 1
        if t & 128: i += nv
        out.append((vs, mat, uv))
    return out

def make_mesh(name, verts_bl, faces, uvs_flat, keep=None):
    faces = [f for f in faces if keep is None or f[1] in keep]
    me = bpy.data.meshes.new(name)
    me.from_pydata([tuple(v) for v in verts_bl], [], [tuple(f[0]) for f in faces])
    uvl = me.uv_layers.new(name="UVMap")
    uv = np.array(uvs_flat, dtype=np.float64).reshape(-1, 2)
    li = 0
    loop_uv = np.zeros((len(me.loops), 2))
    for p, f in zip(me.polygons, faces):
        if f[2] is not None:
            for k, lidx in enumerate(p.loop_indices): loop_uv[lidx] = uv[f[2][k]]
    uvl.data.foreach_set("uv", loop_uv.ravel())
    ob = bpy.data.objects.new(name, me); bpy.context.scene.collection.objects.link(ob)
    for p in me.polygons: p.use_smooth = True
    return ob, faces

bpy.ops.wm.read_factory_settings(use_empty=True)
SC = bpy.context.scene
body_faces = parse_faces(base["faces"])
body_mat_idx = [k for k, m in enumerate(base["materials"]) if m["DbgName"] == "body"]
_bv = sorted({v for f in body_faces if f[1] in body_mat_idx for v in f[0]})
GROUND = float(mh2bl(co[_bv])[:, 2].min())          # sola dos pes vira o chao
body, _ = make_mesh("Body", mh2bl(co), body_faces, base["uvs"][0], keep=set(body_mat_idx))
print("altura: %.2f m" % (mh2bl(co[_bv])[:, 2].max()))

# ------------------------------------------------------------------ esqueleto
sync_helpers()
bones_js = base["bones"]; names = [b["name"] for b in bones_js]
jp = base["metadata"]["joint_pos_idxs"]
def joint(n): return mh2bl(co[jp[n]]).mean(axis=0)
bpy.ops.object.armature_add(location=(0, 0, 0)); arm = bpy.context.object; arm.name = "Rig"
bpy.ops.object.mode_set(mode='EDIT'); eb = arm.data.edit_bones
for b in list(eb): eb.remove(b)
real = [n for n in names if not n.endswith("____head")]
for n in real:
    b = eb.new(n); b.head = Vector(joint(n + "____head")); b.tail = Vector(joint(n + "____tail"))
    if (b.tail - b.head).length < 1e-4: b.tail = b.head + Vector((0, 0, 0.01))
for n in real:
    hi = names.index(n + "____head"); p = bones_js[hi]["parent"]
    if p >= 0:
        pn = names[p].replace("____head", "")
        if pn in eb and pn != n: eb[n].parent = eb[pn]
bpy.ops.object.mode_set(mode='OBJECT')

def skin_groups(ob, sidx, swt, n, remap=None):
    sidx = np.array(sidx).reshape(-1, 4); swt = np.array(swt).reshape(-1, 4)
    groups = {}
    for vi in range(n):
        src = remap[vi] if remap is not None else vi
        for k in range(4):
            w = swt[src, k]
            if w <= 0: continue
            bn = names[sidx[src, k]].replace("____head", "")
            groups.setdefault(bn, ([], []))
            groups[bn][0].append(vi); groups[bn][1].append(w)
    for bn, (ids, ws) in groups.items():
        vg = ob.vertex_groups.get(bn) or ob.vertex_groups.new(name=bn)
        for i, w in zip(ids, ws): vg.add([i], float(w), 'ADD')

skin_groups(body, base["skinIndices"], base["skinWeights"], nverts)

# ------------------------------------------------------------------ proxies
def proxy(path, name, mat_tex, keep_mat=None):
    d = json.load(open(os.path.join(MH_DATA, "proxies", path)))
    ref = np.array(d["ref_vIdxs"]); w = np.array(d["weights"]); off = np.array(d["offsets"])
    pv = (co[ref] * w[:, :, None]).sum(axis=1) + off
    faces = parse_faces(d["faces"])
    ob, _ = make_mesh(name, mh2bl(pv), faces, d["uvs"][0])
    # pesos herdados do corpo pelos vertices de referencia (como o MakeHuman faz)
    BI = np.array(base["skinIndices"]).reshape(-1, 4); BW = np.array(base["skinWeights"]).reshape(-1, 4)
    groups = {}
    for vi in range(len(pv)):
        acc = {}
        for k in range(3):
            r, rw = ref[vi, k], w[vi, k]
            for j in range(4):
                if BW[r, j] > 0:
                    bn = names[BI[r, j]].replace("____head", "")
                    acc[bn] = acc.get(bn, 0) + rw * BW[r, j]
        for bn, ww in acc.items():
            groups.setdefault(bn, []).append((vi, ww))
    for bn, lst in groups.items():
        vg = ob.vertex_groups.new(name=bn)
        for vi, ww in lst: vg.add([vi], float(ww), 'REPLACE')
    return ob
P = lambda *a: os.path.join(MH_DATA, *a)
eyes = proxy("eyes/HighPolyEyes/HighPolyEyes.json", "Eyes", None)
brows = proxy("eyebrows/eyebrow001/eyebrow001.json", "Eyebrows", None)
lashes = proxy("eyelashes/Eyelashes01/Eyelashes01.json", "Eyelashes", None)
teeth = proxy("teeth/Teeth_Base/Teeth_Base.json", "Teeth", None)
hair = proxy(f"hair/{HAIR}/{HAIR}.json", "Hair", None)
outfit = [proxy(f"clothes/{c}/{c}.json", c, None) for c in OUTFIT]

# remove vertices soltos do corpo (helpers do MakeHuman)
bm = bmesh.new(); bm.from_mesh(body.data)
bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context='VERTS')
bm.to_mesh(body.data); bm.free()

# ------------------------------------------------------------------ materiais
def tex_mat(name, img_path, rough=0.5, sss=0.0, alpha=False, bump=0.0, spec=0.5):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = rough
    b.inputs["Specular IOR Level"].default_value = spec
    tx = nt.nodes.new("ShaderNodeTexImage"); tx.image = bpy.data.images.load(img_path)
    nt.links.new(tx.outputs["Color"], b.inputs["Base Color"])
    if alpha:
        nt.links.new(tx.outputs["Alpha"], b.inputs["Alpha"])
        try: m.surface_render_method = 'DITHERED'
        except Exception: pass
    if sss:
        b.inputs["Subsurface Weight"].default_value = sss
        b.inputs["Subsurface Radius"].default_value = (1.0, 0.4, 0.25)
        b.inputs["Subsurface Scale"].default_value = 0.006
    if bump:   # micro relevo de poros
        nz = nt.nodes.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 900; nz.inputs["Detail"].default_value = 6
        bp = nt.nodes.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = bump; bp.inputs["Distance"].default_value = 0.0004
        nt.links.new(nz.outputs["Fac"], bp.inputs["Height"]); nt.links.new(bp.outputs["Normal"], b.inputs["Normal"])
    return m
def set_mat(ob, m):
    ob.data.materials.clear(); ob.data.materials.append(m)
    for p in ob.data.polygons: p.material_index = 0
def skin_material(img_path):
    """Pele: textura + subsurface com raios de pele real + poros/microrrugas + oleosidade variavel."""
    m = bpy.data.materials.new("Skin"); m.use_nodes = True; nt = m.node_tree; N, L = nt.nodes, nt.links
    b = N["Principled BSDF"]
    tc = N.new("ShaderNodeTexCoord")
    tx = N.new("ShaderNodeTexImage"); tx.image = bpy.data.images.load(img_path)
    hs = N.new("ShaderNodeHueSaturation"); hs.inputs["Saturation"].default_value = 1.12; hs.inputs["Value"].default_value = 0.9
    L.new(tx.outputs["Color"], hs.inputs["Color"]); L.new(hs.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Subsurface Weight"].default_value = 0.45
    b.inputs["Subsurface Radius"].default_value = (1.0, 0.37, 0.19)     # proporcao R:G:B de pele real
    b.inputs["Subsurface Scale"].default_value = 0.0045
    b.inputs["Specular IOR Level"].default_value = 0.5
    b.inputs["Coat Weight"].default_value = 0.06; b.inputs["Coat Roughness"].default_value = 0.35
    # oleosidade: rugosidade varia em manchas grandes
    nr = N.new("ShaderNodeTexNoise"); nr.inputs["Scale"].default_value = 35; L.new(tc.outputs["Object"], nr.inputs["Vector"])
    mr = N.new("ShaderNodeMapRange"); mr.inputs["To Min"].default_value = 0.36; mr.inputs["To Max"].default_value = 0.56
    L.new(nr.outputs["Fac"], mr.inputs["Value"]); L.new(mr.outputs["Result"], b.inputs["Roughness"])
    # relevo: poros -> microrrugas -> detalhe da propria textura
    np_ = N.new("ShaderNodeTexNoise"); np_.inputs["Scale"].default_value = 2400; np_.inputs["Detail"].default_value = 2
    L.new(tc.outputs["Object"], np_.inputs["Vector"])
    vo = N.new("ShaderNodeTexVoronoi"); vo.inputs["Scale"].default_value = 700; L.new(tc.outputs["Object"], vo.inputs["Vector"])
    bw = N.new("ShaderNodeRGBToBW"); L.new(tx.outputs["Color"], bw.inputs["Color"])
    prev = None
    for src, out, st, dist in ((np_, "Fac", 0.14, 0.00012), (vo, "Distance", 0.07, 0.0001), (bw, "Val", 0.06, 0.0004)):
        bp = N.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = st; bp.inputs["Distance"].default_value = dist
        L.new(src.outputs[out], bp.inputs["Height"])
        if prev: L.new(prev.outputs["Normal"], bp.inputs["Normal"])
        prev = bp
    L.new(prev.outputs["Normal"], b.inputs["Normal"])
    return m
skin_path = os.path.join(ARA_TEX, SKIN_HD)
if not os.path.exists(skin_path): skin_path = P("skins", SKIN); print("  (sem textura HD, usando 512px)")
set_mat(body, skin_material(skin_path))
eye_path = os.path.join(ARA_TEX, f"eyes_{EYE_COLOR}.png")
if not os.path.exists(eye_path): eye_path = P(f"proxies/eyes/HighPolyEyes/textures/{EYE_COLOR}_eye.png")
em = tex_mat("Eyes", eye_path, 0.15, alpha=True, spec=0.5)
eb_ = em.node_tree.nodes["Principled BSDF"]
eb_.inputs["Coat Weight"].default_value = 1.0; eb_.inputs["Coat Roughness"].default_value = 0.02   # olho "molhado"
set_mat(eyes, em)
set_mat(brows, tex_mat("Eyebrows", P("proxies/eyebrows/eyebrow001/textures/eyebrow001.png"), 0.6, alpha=True))
set_mat(lashes, tex_mat("Eyelashes", P("proxies/eyelashes/Eyelashes01/textures/eyelashes01.png"), 0.6, alpha=True))
set_mat(teeth, tex_mat("Teeth", P("proxies/teeth/Teeth_Base/textures/teeth.png"), 0.3, alpha=True))
set_mat(hair, tex_mat("Hair", P(f"proxies/hair/{HAIR}/textures/{HAIR}_diffuse.png"), 0.7, alpha=True, spec=0.08))
for c, ob in zip(OUTFIT, outfit):
    m = tex_mat(c, P(f"proxies/clothes/{c}/textures/{c}.png"), 0.45)
    if OUTFIT_COLOR:   # cor solida no lugar da textura (a original tem faixas bege)
        b = m.node_tree.nodes["Principled BSDF"]
        for l in list(b.inputs["Base Color"].links): m.node_tree.links.remove(l)
        b.inputs["Base Color"].default_value = OUTFIT_COLOR; b.inputs["Sheen Weight"].default_value = 0.4
    set_mat(ob, m)
    ob.data.polygons.foreach_set("use_smooth", [True] * len(ob.data.polygons))

# ------------------------------------------------------------------ jiggle
# peito: o MakeHuman ja tem ossos breast.L/R com pesos -> renomeia pro padrao do bake_jiggle.py
for s in ("L", "R"):
    arm.data.bones[f"breast.{s}"].name = f"jiggle_breast.{s}"
    for ob in [body] + outfit:
        vg = ob.vertex_groups.get(f"breast.{s}")
        if vg: vg.name = f"jiggle_breast.{s}"
# gluteo: pesos a partir do proprio morph de volume do gluteo (onde ele mexe = onde balanca)
gi, gv = tdelta("buttocks/buttocks-volume-incr")
mag = np.linalg.norm(gv, axis=1); mag /= mag.max()
gw = np.zeros(nverts); gw[gi] = np.clip(mag * 1.6, 0, 1) ** 0.8
gpos = mh2bl(co)
bpy.context.view_layer.objects.active = arm; bpy.ops.object.mode_set(mode='EDIT')
for s, sg in (("L", 1), ("R", -1)):
    side = (gpos[:, 0] * sg > 0) & (gw > 0.05)
    c = (gpos[side] * gw[side, None]).sum(0) / gw[side].sum()
    b = arm.data.edit_bones.new(f"jiggle_glute.{s}")
    b.head = Vector((c[0], c[1] - 0.05, c[2])); b.tail = Vector((c[0], c[1] + 0.06, c[2] - 0.01))
    b.parent = arm.data.edit_bones["pelvis." + s]
bpy.ops.object.mode_set(mode='OBJECT')
def add_glute(ob, positions, weights_by_vert):
    for s, sg in (("L", 1), ("R", -1)):
        vg = ob.vertex_groups.new(name=f"jiggle_glute.{s}")
        for vi in range(len(positions)):
            w = weights_by_vert[vi]
            if w <= 0.02 or positions[vi][0] * sg <= 0: continue
            for g in ob.data.vertices[vi].groups:
                if g.group != vg.index: g.weight *= (1 - w)
            vg.add([vi], float(w), 'REPLACE')
# indices do corpo mudaram ao remover helpers -> casa pela posicao
from mathutils import kdtree
kd = kdtree.KDTree(nverts)
for i, p in enumerate(gpos): kd.insert(Vector(p), i)
kd.balance()
bv = [v.co.copy() for v in body.data.vertices]
add_glute(body, bv, [gw[kd.find(p)[1]] for p in bv])

# ------------------------------------------------------------------ roupa por fora do corpo
# os proxies foram feitos pra base; com busto/gluteo maiores o corpo atravessaria o tecido
for ob in outfit:
    bpy.ops.object.select_all(action='DESELECT'); bpy.context.view_layer.objects.active = ob; ob.select_set(True)
    sw = ob.modifiers.new("Shrinkwrap", 'SHRINKWRAP'); sw.target = body
    sw.wrap_method = 'NEAREST_SURFACEPOINT'; sw.wrap_mode = 'OUTSIDE'; sw.offset = 0.0025
    bpy.ops.object.modifier_apply(modifier="Shrinkwrap")
    sm = ob.modifiers.new("Smooth", 'CORRECTIVE_SMOOTH'); sm.factor = 0.5; sm.iterations = 4
    bpy.ops.object.modifier_apply(modifier="Smooth")
    sw = ob.modifiers.new("Shrinkwrap", 'SHRINKWRAP'); sw.target = body
    sw.wrap_method = 'NEAREST_SURFACEPOINT'; sw.wrap_mode = 'OUTSIDE'; sw.offset = 0.0025
    bpy.ops.object.modifier_apply(modifier="Shrinkwrap")

# ------------------------------------------------------------------ amarra tudo no rig
for ob in [body, eyes, brows, lashes, teeth, hair] + outfit:
    ob.parent = arm
    am = ob.modifiers.new("Armature", 'ARMATURE'); am.object = arm
for ob in [body] + outfit:
    ss = ob.modifiers.new("Subdivision", 'SUBSURF'); ss.levels = 1; ss.render_levels = 2
for ob in outfit:   # mantem o tecido por fora do corpo depois da subdivisao e em qualquer pose
    sw = ob.modifiers.new("KeepOutside", 'SHRINKWRAP'); sw.target = body
    sw.wrap_method = 'NEAREST_SURFACEPOINT'; sw.wrap_mode = 'OUTSIDE'; sw.offset = 0.002
bpy.context.view_layer.objects.active = body
bpy.ops.object.vertex_group_limit_total(group_select_mode='ALL', limit=4)
bpy.ops.object.vertex_group_normalize_all(group_select_mode='ALL', lock_active=False)

print("corpo:", len(body.data.vertices), "vertices |", "ossos:", len(arm.data.bones))
bpy.ops.file.pack_all()
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "mh_character.blend"))
bpy.ops.export_scene.gltf(filepath=os.path.join(HERE, "mh_character.glb"), export_format='GLB')
print("OK")
