"""Cabelo de fios (curvas) gerado a partir das placas do cabelo do MakeHuman.
Cada placa vira uma linha-guia; em cima de cada guia nascem varios fios, com variacao e
pontas soltas. Material: Principled Hair BSDF (realista no Cycles).
As placas ficam no arquivo (escondidas no render) pra uso em jogo.
Rodar: python build_hair.py [guias]   (le e salva mh_character.blend)"""
import bpy, bmesh, math, os, sys
import numpy as np
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
STRAND_SPACING = 0.0007   # distancia media entre fios na largura da placa (m)
POINTS = 18               # pontos por fio
RADIUS = 0.00012          # raio do fio (m)
MELANIN, REDNESS = 0.85, 0.32
SEED = 7
N_STRANDS = 30000        # quantidade de fios
ONLY_GUIDES = "guias" in sys.argv

bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE, "mh_character.blend"))
arm = bpy.data.objects["Rig"]; cards = bpy.data.objects["Hair"]
for n in ("HairStrands",):
    if n in bpy.data.objects: bpy.data.objects.remove(bpy.data.objects[n])
rng = np.random.default_rng(SEED)

# ---- ilhas (placas) e coordenadas
bm = bmesh.new(); bm.from_mesh(cards.data); bm.verts.ensure_lookup_table()
uvl = bm.loops.layers.uv.active
vuv = np.zeros((len(bm.verts), 2)); cnt = np.zeros(len(bm.verts))
for f in bm.faces:
    for l in f.loops: vuv[l.vert.index] += l[uvl].uv; cnt[l.vert.index] += 1
vuv /= np.maximum(cnt, 1)[:, None]
pos = np.array([v.co[:] for v in bm.verts])
seen = np.zeros(len(bm.verts), bool); islands = []
for v in bm.verts:
    if seen[v.index] or not v.link_faces: continue
    stack, isl = [v], []
    seen[v.index] = True
    while stack:
        x = stack.pop(); isl.append(x.index)
        for e in x.link_edges:
            o = e.other_vert(x)
            if not seen[o.index]: seen[o.index] = True; stack.append(o)
    islands.append(np.array(isl))
head = arm.pose.bones["head"]; hc = (head.head + head.tail) / 2
hc = np.array(hc[:]) + np.array([0, 0.01, -0.03])
print("placas:", len(islands))

def resample(pts, n):
    d = np.r_[0, np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))]
    if d[-1] < 1e-6: return None
    t = np.linspace(0, d[-1], n)
    return np.stack([np.interp(t, d, pts[:, k]) for k in range(3)], axis=1)

# direcao do fio em cada face: na textura os fios correm no eixo V, raiz em cima (V alto)
from mathutils.bvhtree import BVHTree
bm.faces.ensure_lookup_table()
along = np.zeros((len(bm.faces), 3)); fnorm = np.zeros((len(bm.faces), 3)); farea = np.zeros(len(bm.faces))
for f in bm.faces:
    l0, l1, l2 = f.loops[0], f.loops[1], f.loops[2]
    e1 = np.array(l1.vert.co - l0.vert.co); e2 = np.array(l2.vert.co - l0.vert.co)
    du1, dv1 = l1[uvl].uv - l0[uvl].uv; du2, dv2 = l2[uvl].uv - l0[uvl].uv
    det = du1 * dv2 - du2 * dv1
    if abs(det) < 1e-12: continue
    dpdv = (-du2 * e1 + du1 * e2) / det
    n = np.linalg.norm(dpdv)
    if n > 0: along[f.index] = -dpdv / n          # da raiz pra ponta
    fnorm[f.index] = f.normal[:]; farea[f.index] = f.calc_area()
bvh = BVHTree.FromBMesh(bm)
STEP = 0.004

def trace(p0, sign):
    pts, p, prev = [], Vector(p0), None
    for _ in range(400):
        hit = bvh.find_nearest(p)
        if hit[0] is None or hit[3] > 0.004: break
        d = along[hit[2]] * sign
        if not d.any(): break
        if prev is not None and np.dot(d, prev) < 0.2: break   # virada brusca = saiu da lamina
        p = hit[0] + Vector(d) * STEP; prev = d; pts.append(np.array(hit[0][:]))
    return pts

guides = []
nseed = 60 if ONLY_GUIDES else N_STRANDS
prob = farea / farea.sum()
faces_idx = rng.choice(len(farea), size=nseed, p=prob)
for fi in faces_idx:
    f = bm.faces[int(fi)]
    w = rng.dirichlet([1, 1, 1]); vs = [v.co for v in f.verts[:3]]
    p0 = vs[0] * w[0] + vs[1] * w[1] + vs[2] * w[2]
    back = trace(p0, -1); fwd = trace(p0, 1)
    p = np.array(back[::-1] + fwd[1:]) if back and fwd else None
    if p is None or len(p) < 6: continue
    if np.linalg.norm(p[-1] - hc) < np.linalg.norm(p[0] - hc): p = p[::-1]
    if np.linalg.norm(np.diff(p, axis=0), axis=1).sum() < 0.04: continue
    off = fnorm[int(fi)] * rng.uniform(0, 0.007)            # volume: afasta um pouco da casca
    p = resample(p + off, POINTS)
    if p is not None: guides.append(p)
print("linhas:", len(guides))

# ---- fios
strands = []
s_ = np.linspace(0, 1, POINTS)[:, None]
# centros de mechas: fios proximos puxam pro mesmo centro na ponta (efeito de mecha)
G = np.array(guides); tips = G[:, -1]
nclump = max(1, len(G) // 60)
cent = tips[rng.choice(len(G), nclump, replace=False)]
from mathutils import kdtree
kdc = kdtree.KDTree(nclump)
for i, p in enumerate(cent): kdc.insert(Vector(p), i)
kdc.balance()
for c in guides:
    if not ONLY_GUIDES:
        _, ci, _ = kdc.find(Vector(c[-1]))
        pull = (cent[ci] - c[-1]) * rng.uniform(0.3, 0.7)             # mecha
        c = c + pull * s_ ** 1.5
        wave = np.sin(s_ * rng.uniform(5, 9) + rng.uniform(0, 6.28)) * 0.004 * s_   # leve ondulado
        side = np.cross(c[-1] - c[0], [0, 0, 1]); side /= np.linalg.norm(side) + 1e-9
        c = c + wave * side
        fly = rng.random() < 0.04                                      # fios soltos
        frizz = np.cumsum(rng.normal(0, 1, (POINTS, 3)) * (0.0004 + (0.012 if fly else 0.004) * s_ ** 2.5), axis=0) * 0.35
        c = c + frizz * s_
        if rng.random() < 0.7:                                    # pontas desiguais
            c = resample(c[: max(3, int(POINTS * rng.uniform(0.72, 1.0)))], POINTS)
    if c is not None: strands.append(c)
strands = np.array(strands)
print("fios:", len(strands))

# ---- objeto Curves
cv = bpy.data.hair_curves.new("HairStrands")
cv.add_curves([POINTS] * len(strands))
cv.attributes["position"].data.foreach_set("vector", strands.reshape(-1).astype(np.float32))
rad = cv.attributes.get("radius") or cv.attributes.new("radius", 'FLOAT', 'POINT')
taper = np.tile(np.linspace(1.0, 0.35, POINTS), len(strands)) * RADIUS * (8 if ONLY_GUIDES else 1)
rad.data.foreach_set("value", taper.astype(np.float32))
ob = bpy.data.objects.new("HairStrands", cv); bpy.context.scene.collection.objects.link(ob)

m = bpy.data.materials.get("HairStrands") or bpy.data.materials.new("HairStrands")
m.use_nodes = True; nt = m.node_tree
for nd in list(nt.nodes):
    if nd.type != 'OUTPUT_MATERIAL': nt.nodes.remove(nd)
hb = nt.nodes.new("ShaderNodeBsdfHairPrincipled"); hb.parametrization = 'MELANIN'
for k, v in {"Melanin": MELANIN, "Melanin Redness": REDNESS, "Roughness": 0.28,
             "Radial Roughness": 0.35, "Coat": 0.15, "Random Roughness": 0.25, "Random Color": 0.12}.items():
    if k in hb.inputs: hb.inputs[k].default_value = v
nt.links.new(hb.outputs[0], nt.nodes["Material Output"].inputs["Surface"])
cv.materials.append(m)

# segue a cabeca
bpy.ops.object.select_all(action='DESELECT')
ob.select_set(True); arm.select_set(True); bpy.context.view_layer.objects.active = arm
arm.data.bones.active = arm.data.bones["head"]
bpy.ops.object.parent_set(type='BONE', keep_transform=True)
cards.hide_render = True          # placas ficam pro jogo
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "mh_character.blend"))
print("OK")
