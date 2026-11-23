"""Modelo realista (estilizado) de mulher adulta, neutro (sem genitais/mamilos).
Corpo: Skin + Subsurf nivel 3 + esculpido procedural (rosto, umbigo). Olhos, orelhas,
sobrancelhas, cabelo, rig com dedos/dedos do pe e ossos de jiggle, pesos automaticos.
Rodar: python build_character.py   (modulo bpy)"""
import bpy, math, os
import numpy as np
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.read_factory_settings(use_empty=True)
SC = bpy.context.scene
AZ = 1.375   # altura dos bracos em T-pose

# ------------------------------------------------------------ esqueleto da malha
V, E, R, IDX = [], [], [], {}
def vert(name, co, r):
    IDX[name] = len(V); V.append(Vector(co)); R.append(r); return name
def chain(*names):
    for a, b in zip(names, names[1:]): E.append((IDX[a], IDX[b]))

vert("pelvis", (0, 0.005, 0.955), (0.118, 0.092))
vert("waist",  (0, 0.000, 1.065), (0.105, 0.075))
vert("ribs",   (0, 0.000, 1.185), (0.125, 0.088))
vert("chest",  (0, 0.000, 1.285), (0.142, 0.095))
vert("neckb",  (0, 0.000, 1.415), (0.052, 0.052))
vert("neck",   (0, 0.008, 1.475), (0.047, 0.049))
vert("chin",   (0, -0.040, 1.502), (0.046, 0.046))
vert("head",   (0, 0.000, 1.588), (0.100, 0.104))
vert("jaw.L", (0.045, -0.012, 1.515), (0.042, 0.042)); vert("jaw.R", (-0.045, -0.012, 1.515), (0.042, 0.042))
vert("crown",  (0, 0.006, 1.665), (0.072, 0.080))
chain("pelvis", "waist", "ribs", "chest", "neckb", "neck", "chin", "head", "crown")
for j in ("jaw.L", "jaw.R"): E.append((IDX["chin"], IDX[j]))   # ramos (sem fechar lacos: o Skin faz buracos)

FING = {}
OFF_TOE = (-0.024, -0.008, 0.007, 0.020, 0.030)
R_TOE = (0.0125, 0.009, 0.0085, 0.0075, 0.0065)
Y_TOE = (-0.176, -0.181, -0.173, -0.163, -0.150)
for s, x in (("L", 1), ("R", -1)):
    vert(f"shoulder.{s}", (0.165*x, 0, AZ), (0.048, 0.050)); E.append((IDX["chest"], IDX[f"shoulder.{s}"]))
    vert(f"uarm.{s}",  (0.31*x, 0, AZ), (0.041, 0.042))
    vert(f"elbow.{s}", (0.45*x, 0, AZ), (0.034, 0.033))
    vert(f"farm.{s}",  (0.56*x, 0, AZ), (0.032, 0.030))
    vert(f"wrist.{s}", (0.69*x, 0, AZ), (0.024, 0.017))
    vert(f"palm.{s}",  (0.755*x, 0, AZ), (0.033, 0.011))
    chain(f"shoulder.{s}", f"uarm.{s}", f"elbow.{s}", f"farm.{s}", f"wrist.{s}", f"palm.{s}")
    for i, (dy, ln, rad) in enumerate(((-0.020, 0.074, 0.0085), (-0.007, 0.082, 0.009),
                                       (0.006, 0.074, 0.0085), (0.019, 0.060, 0.0075))):
        b = (0.772*x, dy, AZ); m = ((0.772 + ln*0.5)*x, dy*1.1, AZ - 0.004); t = ((0.772 + ln)*x, dy*1.2, AZ - 0.013)
        vert(f"fb{i}.{s}", b, (rad, rad)); vert(f"fm{i}.{s}", m, (rad*0.9, rad*0.9)); vert(f"ft{i}.{s}", t, (rad*0.75, rad*0.75))
        chain(f"palm.{s}", f"fb{i}.{s}", f"fm{i}.{s}", f"ft{i}.{s}"); FING[f"finger{i}.{s}"] = (b, t)
    tb = (0.735*x, -0.020, AZ - 0.003); tm = (0.765*x, -0.042, AZ - 0.006); tt = (0.787*x, -0.060, AZ - 0.010)
    vert(f"tb.{s}", tb, (0.0115, 0.0115)); vert(f"tm.{s}", tm, (0.0105, 0.0105)); vert(f"tt.{s}", tt, (0.0095, 0.0095))
    chain(f"palm.{s}", f"tb.{s}", f"tm.{s}", f"tt.{s}"); FING[f"finger4.{s}"] = (tb, tt)

    vert(f"hip.{s}",   (0.088*x, 0.005, 0.868), (0.082, 0.090))
    vert(f"thigh.{s}", (0.088*x, 0.000, 0.715), (0.080, 0.084))
    vert(f"lthigh.{s}",(0.088*x, 0.000, 0.585), (0.062, 0.066))
    vert(f"knee.{s}",  (0.088*x, 0.000, 0.490), (0.050, 0.055))
    vert(f"calf.{s}",  (0.089*x, 0.012, 0.365), (0.052, 0.062))
    vert(f"lcalf.{s}", (0.090*x, 0.008, 0.225), (0.036, 0.040))
    vert(f"ankle.{s}", (0.090*x, 0.005, 0.085), (0.028, 0.030))
    vert(f"heel.{s}",  (0.090*x, 0.040, 0.034), (0.030, 0.028))
    vert(f"ball.{s}",  (0.092*x, -0.100, 0.030), (0.040, 0.026))
    chain("pelvis", f"hip.{s}", f"thigh.{s}", f"lthigh.{s}", f"knee.{s}", f"calf.{s}", f"lcalf.{s}", f"ankle.{s}")
    chain(f"ankle.{s}", f"heel.{s}"); chain(f"ankle.{s}", f"ball.{s}")
    for i in range(5):
        vert(f"toe{i}.{s}", (0.092*x + OFF_TOE[i]*x, Y_TOE[i], 0.020), (R_TOE[i], 0.016))
        chain(f"ball.{s}", f"toe{i}.{s}")
    vert(f"bst.{s}",  (0.072*x, -0.060, 1.262), (0.066, 0.056)); chain("chest", f"bst.{s}")
    vert(f"bstt.{s}", (0.074*x, -0.100, 1.252), (0.042, 0.038)); chain(f"bst.{s}", f"bstt.{s}")
    vert(f"gl.{s}",   (0.070*x, 0.085, 0.905), (0.078, 0.085)); chain(f"hip.{s}", f"gl.{s}")
    vert(f"glt.{s}",  (0.070*x, 0.115, 0.880), (0.058, 0.056)); chain(f"gl.{s}", f"glt.{s}")

me = bpy.data.meshes.new("BodyMesh"); me.from_pydata([tuple(v) for v in V], E, [])
body = bpy.data.objects.new("Body", me); SC.collection.objects.link(body)
bpy.context.view_layer.objects.active = body; body.select_set(True)
sk = body.modifiers.new("Skin", 'SKIN'); sk.use_smooth_shade = True
for i, d in enumerate(me.skin_vertices[0].data):
    d.radius = R[i]; d.use_root = (i == IDX["pelvis"])
ss = body.modifiers.new("Subsurf", 'SUBSURF'); ss.levels = 3; ss.render_levels = 3
for m in ("Skin", "Subsurf"): bpy.ops.object.modifier_apply(modifier=m)

# ------------------------------------------------------------ esculpido procedural
import bmesh
bm = bmesh.new(); bm.from_mesh(me)
for _ in range(2):   # mais densidade so no rosto, pra caber nariz/labios/orbitas
    edges = [e for e in bm.edges if all(v.co.z > 1.47 and v.co.y < 0.02 and abs(v.co.x) < 0.075 for v in e.verts)]
    bmesh.ops.subdivide_edges(bm, edges=edges, cuts=1, use_grid_fill=True)
bmesh.ops.recalc_face_normals(bm, faces=bm.faces)   # o Skin deixa faces invertidas nas juncoes
bm.to_mesh(me); bm.free(); me.update()
n = len(me.vertices); co = np.empty(n*3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
def bump(cx, cz, sx, sz, amp, zr=None):
    """Desloca a frente (y<0) em torno de (cx,cz): amp>0 pra fora, <0 pra dentro."""
    for sgn in ((1, -1) if cx != 0 else (1,)):
        d = np.exp(-(((co[:, 0] - cx*sgn)/sx)**2 + ((co[:, 2] - cz)/sz)**2))
        co[:, 1] -= amp * d * (co[:, 1] < 0.0)
bump(0, 1.552, 0.010, 0.012, 0.017)      # ponta do nariz
bump(0, 1.578, 0.008, 0.020, 0.008)      # dorso do nariz
bump(0.015, 1.548, 0.008, 0.008, 0.006)  # asas do nariz
bump(0, 1.535, 0.010, 0.005, -0.003)     # filtro
bump(0, 1.525, 0.021, 0.0045, 0.008)     # labio superior
bump(0, 1.510, 0.019, 0.0055, 0.009)     # labio inferior
bump(0, 1.5175, 0.022, 0.0015, -0.004)   # linha da boca
bump(0.036, 1.590, 0.017, 0.009, -0.007) # orbitas
bump(0.034, 1.612, 0.023, 0.006, 0.006)  # arcada
bump(0.052, 1.558, 0.018, 0.014, 0.004)  # macas do rosto
bump(0, 1.478, 0.017, 0.012, 0.006)      # queixo
bump(0, 1.002, 0.007, 0.007, -0.007)     # umbigo
me.vertices.foreach_set('co', co.ravel()); me.update()
bpy.ops.object.shade_smooth()

def surf_y(x, z, tol=0.004):
    while True:
        sel = (np.abs(co[:, 0]-x) < tol) & (np.abs(co[:, 2]-z) < tol) & (co[:, 1] < 0.02) & (co[:, 2] > 1.4)
        if sel.any(): return co[sel, 1].min()
        tol *= 1.6

def mat(name, color, rough=0.5, sss=0.0, extra=None):
    m = bpy.data.materials.new(name); m.diffuse_color = color; m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = color; b.inputs["Roughness"].default_value = rough
    if sss:
        b.inputs["Subsurface Weight"].default_value = sss
        b.inputs["Subsurface Radius"].default_value = (1.0, 0.35, 0.2)
        b.inputs["Subsurface Scale"].default_value = 0.012
    for k, v in (extra or {}).items(): b.inputs[k].default_value = v
    return m
skin = mat("Skin", (0.80, 0.56, 0.44, 1), 0.48, 0.35, {"Specular IOR Level": 0.35})
lips = mat("Lips", (0.62, 0.26, 0.28, 1), 0.38, 0.2)
body.data.materials.append(skin); body.data.materials.append(lips)
pc = np.empty(len(me.polygons)*3); me.polygons.foreach_get('center', pc); pc = pc.reshape(-1, 3)
inl = ((pc[:, 0]/0.024)**2 + ((pc[:, 2]-1.518)/0.0125)**2 < 1) & (pc[:, 1] < -0.06)
mi = np.zeros(len(me.polygons), dtype=np.int32); mi[inl] = 1; me.polygons.foreach_set('material_index', mi)
print("corpo:", n, "vertices")

# ------------------------------------------------------------ olhos, orelhas, sobrancelhas, cabelo
parts = []
def prim(name, loc, scale, material, rot=None):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=14, location=loc)
    o = bpy.context.object; o.name = name; o.scale = scale
    if rot: o.rotation_euler = rot
    bpy.ops.object.transform_apply(scale=True, rotation=True)
    o.data.materials.append(material); bpy.ops.object.shade_smooth(); parts.append(o); return o
sclera = mat("Sclera", (0.93, 0.92, 0.9, 1), 0.12); iris = mat("Iris", (0.28, 0.17, 0.08, 1), 0.2)
pupil = mat("Pupil", (0.01, 0.01, 0.01, 1), 0.1)
hair_m = mat("Hair", (0.16, 0.085, 0.045, 1), 0.38, 0, {"Anisotropic": 0.3})
brow_m = mat("Brow", (0.12, 0.065, 0.035, 1), 0.5)
er = 0.0115
for s, x in (("L", 1), ("R", -1)):
    ey = surf_y(0.036*x, 1.590) - 0.003 + er
    prim(f"eye.{s}", (0.036*x, ey, 1.590), (er, er, er), sclera)
    prim(f"iris.{s}", (0.036*x, ey - er*0.93, 1.590), (0.0062, 0.0022, 0.0062), iris)
    prim(f"pupil.{s}", (0.036*x, ey - er*0.97, 1.590), (0.0029, 0.0014, 0.0029), pupil)
    by = surf_y(0.034*x, 1.614) + 0.001
    prim(f"brow.{s}", (0.034*x, by, 1.614), (0.0175, 0.0042, 0.0034), brow_m, (0, 0, math.radians(-8*x)))
    prim(f"ear.{s}", (0.0825*x, 0.012, 1.585), (0.0055, 0.016, 0.025), skin)
hair = prim("hair_cap", (0, 0.012, 1.603), (0.090, 0.104, 0.092), hair_m)
import bmesh
bm = bmesh.new(); bm.from_mesh(hair.data)
cut = [v for v in bm.verts if (v.co.y < -0.035 and v.co.z < 1.650) or (v.co.z < 1.575 and v.co.y < 0.03)]
bmesh.ops.delete(bm, geom=cut, context='VERTS'); bm.to_mesh(hair.data); bm.free()
sol = hair.modifiers.new('Solidify', 'SOLIDIFY'); sol.thickness = 0.006; sol.offset = 1
bpy.context.view_layer.objects.active = hair; bpy.ops.object.modifier_apply(modifier='Solidify')
prim("hair_back", (0, 0.070, 1.495), (0.088, 0.062, 0.185), hair_m)
for s, x in (("L", 1), ("R", -1)):
    prim(f"hair_side.{s}", (0.080*x, 0.040, 1.550), (0.016, 0.040, 0.075), hair_m)
bpy.ops.object.select_all(action='DESELECT')
for o in parts: o.select_set(True)
bpy.context.view_layer.objects.active = parts[0]; bpy.ops.object.join()
face = bpy.context.object; face.name = "FaceHair"

# ------------------------------------------------------------ armature
bpy.ops.object.armature_add(location=(0, 0, 0)); arm = bpy.context.object; arm.name = "Rig"
bpy.ops.object.mode_set(mode='EDIT'); eb = arm.data.edit_bones
for b in list(eb): eb.remove(b)
def bone(name, head, tail, parent=None, connect=False):
    b = eb.new(name); b.head = head; b.tail = tail
    if parent: b.parent = eb[parent]; b.use_connect = connect
bone("pelvis", (0, 0, 0.92), (0, 0, 1.00))
bone("spine", (0, 0, 1.00), (0, 0, 1.19), "pelvis", True)
bone("chest", (0, 0, 1.19), (0, 0, 1.41), "spine", True)
bone("neck", (0, 0, 1.41), (0, 0, 1.49), "chest", True)
bone("head", (0, 0, 1.49), (0, 0, 1.70), "neck", True)
for s, x in (("L", 1), ("R", -1)):
    bone(f"clavicle.{s}", (0, 0, AZ), (0.165*x, 0, AZ), "chest")
    bone(f"upperarm.{s}", (0.165*x, 0, AZ), (0.45*x, 0, AZ), f"clavicle.{s}", True)
    bone(f"forearm.{s}", (0.45*x, 0, AZ), (0.69*x, 0, AZ), f"upperarm.{s}", True)
    bone(f"hand.{s}", (0.69*x, 0, AZ), (0.772*x, 0, AZ), f"forearm.{s}", True)
    for i in range(5):
        h, t = FING[f"finger{i}.{s}"]; bone(f"finger{i}.{s}", h, t, f"hand.{s}")
    bone(f"thigh.{s}", (0.08*x, 0, 0.90), (0.088*x, 0, 0.49), "pelvis")
    bone(f"shin.{s}", (0.088*x, 0, 0.49), (0.09*x, 0.005, 0.085), f"thigh.{s}", True)
    bone(f"foot.{s}", (0.09*x, 0.005, 0.085), (0.092*x, -0.100, 0.03), f"shin.{s}", True)
    bone(f"toe.{s}", (0.092*x, -0.100, 0.03), (0.092*x, -0.18, 0.02), f"foot.{s}", True)
    bone(f"jiggle_breast.{s}", (0.072*x, -0.045, 1.262), (0.074*x, -0.14, 1.250), "chest")
    bone(f"jiggle_glute.{s}", (0.070*x, 0.05, 0.905), (0.070*x, 0.15, 0.880), "pelvis")
bpy.ops.object.mode_set(mode='OBJECT')

# ------------------------------------------------------------ pesos
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True); arm.select_set(True); bpy.context.view_layer.objects.active = arm
bpy.ops.object.parent_set(type='ARMATURE_AUTO')
assert len(body.vertex_groups) > 0, "pesos automaticos falharam"
def smooth_weights(factor=0.6, repeat=10):
    """Suaviza os pesos pelos vizinhos da malha (evita a transicao abrupta que rasga o quadril)."""
    nv, ng = len(body.data.vertices), len(body.vertex_groups)
    W = np.zeros((nv, ng))
    for v in body.data.vertices:
        for g in v.groups: W[v.index, g.group] = g.weight
    ev = np.array([e.vertices[:] for e in body.data.edges]); deg = np.bincount(ev.ravel(), minlength=nv)[:, None]
    for _ in range(repeat):
        S = np.zeros_like(W); np.add.at(S, ev[:, 0], W[ev[:, 1]]); np.add.at(S, ev[:, 1], W[ev[:, 0]])
        W = (1 - factor) * W + factor * S / np.maximum(deg, 1)
    for gi, vg in enumerate(body.vertex_groups):
        vg.remove(list(range(nv)))
        for i in np.nonzero(W[:, gi] > 1e-3)[0]: vg.add([int(i)], float(W[i, gi]), 'REPLACE')
smooth_weights()
def blend_group(vg_name, center, radius):
    vg = body.vertex_groups[vg_name]; c = Vector(center)
    for v in body.data.vertices:
        dist = (v.co - c).length
        if dist >= radius: continue
        w = 1.0 if dist < radius*0.5 else (radius - dist)/(radius*0.5)
        for g in v.groups:
            if g.group != vg.index: g.weight *= (1 - w)
        vg.add([v.index], w, 'REPLACE')
for s, x in (("L", 1), ("R", -1)):
    blend_group(f"jiggle_breast.{s}", (0.074*x, -0.092, 1.255), 0.095)
    blend_group(f"jiggle_glute.{s}", (0.070*x, 0.100, 0.890), 0.125)
bpy.context.view_layer.objects.active = body
bpy.ops.object.vertex_group_limit_total(group_select_mode='ALL', limit=4)
bpy.ops.object.vertex_group_normalize_all(group_select_mode='ALL', lock_active=False)
vg = face.vertex_groups.new(name="head"); vg.add(list(range(len(face.data.vertices))), 1.0, 'REPLACE')
face.parent = arm; face.modifiers.new("Armature", 'ARMATURE').object = arm

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "character_model.blend"))
bpy.ops.export_scene.gltf(filepath=os.path.join(HERE, "character_model.glb"), export_format='GLB')
print("OK")
