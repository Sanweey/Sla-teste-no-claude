"""Modelo completo da boneca: corpo suave (Skin + Subsurf), mãos com dedos, pés, rosto
basico, cabelo, rig com dedos e ossos de jiggle, pesos automaticos.
Neutro (sem genitais). Rodar: python build_character.py   (modulo bpy)"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.read_factory_settings(use_empty=True)
SC = bpy.context.scene

# ---------------------------------------------------------------- corpo (Skin)
V, E, R = [], [], []          # vertices, arestas, raios (rx, ry)
IDX = {}
def vert(name, co, r):
    IDX[name] = len(V); V.append(Vector(co)); R.append(r); return name
def edge(a, b): E.append((IDX[a], IDX[b]))

vert("pelvis", (0, 0.005, 0.97), (0.135, 0.095))
vert("waist",  (0, 0.000, 1.10), (0.115, 0.080))
vert("ribs",   (0, 0.000, 1.21), (0.135, 0.090))
vert("chest",  (0, 0.000, 1.31), (0.150, 0.095))
vert("neckb",  (0, 0.000, 1.43), (0.050, 0.050))
vert("neck",   (0, 0.005, 1.50), (0.048, 0.050))
vert("chin",   (0, -0.030, 1.555), (0.060, 0.060))
vert("head",   (0, 0.000, 1.625), (0.092, 0.104))
vert("crown",  (0, 0.005, 1.690), (0.065, 0.075))
for a, b in (("pelvis","waist"),("waist","ribs"),("ribs","chest"),("chest","neckb"),
             ("neckb","neck"),("neck","chin"),("chin","head"),("head","crown")): edge(a, b)

FING = {}   # nome -> (palma, ponta) por lado, para criar ossos depois
for s, x in (("L", 1), ("R", -1)):
    vert(f"shoulder.{s}", (0.17*x, 0, 1.395), (0.050, 0.050)); edge("chest", f"shoulder.{s}")
    vert(f"elbow.{s}",    (0.45*x, 0, 1.395), (0.040, 0.040)); edge(f"shoulder.{s}", f"elbow.{s}")
    vert(f"wrist.{s}",    (0.69*x, 0, 1.395), (0.029, 0.025)); edge(f"elbow.{s}", f"wrist.{s}")
    vert(f"palm.{s}",     (0.755*x, 0, 1.395), (0.034, 0.012)); edge(f"wrist.{s}", f"palm.{s}")
    # dedos: indicador, medio, anelar, mindinho + polegar
    for i, (dy, ln, rad) in enumerate(((-0.020, 0.072, 0.0085), (-0.007, 0.080, 0.009),
                                       (0.006, 0.072, 0.0085), (0.019, 0.058, 0.0075))):
        base = (0.775*x, dy, 1.395); tip = ((0.775 + ln) * x, dy*1.2, 1.395)
        vert(f"fb{i}.{s}", base, (rad, rad)); vert(f"ft{i}.{s}", tip, (rad*0.8, rad*0.8))
        edge(f"palm.{s}", f"fb{i}.{s}"); edge(f"fb{i}.{s}", f"ft{i}.{s}")
        FING[f"finger{i}.{s}"] = (base, tip)
    tb = (0.735*x, -0.018, 1.392); tt = (0.785*x, -0.058, 1.385)
    vert(f"tb.{s}", tb, (0.011, 0.011)); vert(f"tt.{s}", tt, (0.0095, 0.0095))
    edge(f"palm.{s}", f"tb.{s}"); edge(f"tb.{s}", f"tt.{s}"); FING[f"finger4.{s}"] = (tb, tt)

    vert(f"hip.{s}",   (0.075*x, 0.005, 0.925), (0.078, 0.088)); edge("pelvis", f"hip.{s}")
    vert(f"thigh.{s}", (0.088*x, 0, 0.72), (0.078, 0.082)); edge(f"hip.{s}", f"thigh.{s}")
    vert(f"knee.{s}",  (0.090*x, 0, 0.50), (0.056, 0.058)); edge(f"thigh.{s}", f"knee.{s}")
    vert(f"calf.{s}",  (0.090*x, 0.010, 0.33), (0.052, 0.058)); edge(f"knee.{s}", f"calf.{s}")
    vert(f"ankle.{s}", (0.090*x, 0.005, 0.085), (0.032, 0.034)); edge(f"calf.{s}", f"ankle.{s}")
    vert(f"heel.{s}",  (0.090*x, 0.040, 0.035), (0.030, 0.028)); edge(f"ankle.{s}", f"heel.{s}")
    vert(f"ball.{s}",  (0.092*x, -0.095, 0.030), (0.040, 0.026)); edge(f"ankle.{s}", f"ball.{s}")
    vert(f"toe.{s}",   (0.092*x, -0.165, 0.022), (0.032, 0.020)); edge(f"ball.{s}", f"toe.{s}")
    # peito e gluteo: ramos curtos (os ossos de jiggle ficam nessas regioes)
    vert(f"bst.{s}",   (0.082*x, -0.065, 1.285), (0.070, 0.058)); edge("chest", f"bst.{s}")
    vert(f"bstt.{s}",  (0.084*x, -0.105, 1.280), (0.048, 0.040)); edge(f"bst.{s}", f"bstt.{s}")
    vert(f"gl.{s}",    (0.070*x, 0.085, 0.925), (0.078, 0.085)); edge(f"hip.{s}", f"gl.{s}")
    vert(f"glt.{s}",   (0.070*x, 0.115, 0.900), (0.060, 0.060)); edge(f"gl.{s}", f"glt.{s}")

me = bpy.data.meshes.new("BodyMesh"); me.from_pydata([tuple(v) for v in V], E, [])
body = bpy.data.objects.new("Body", me); SC.collection.objects.link(body)
bpy.context.view_layer.objects.active = body; body.select_set(True)
sk = body.modifiers.new("Skin", 'SKIN'); sk.use_smooth_shade = True
layer = me.skin_vertices[0]
for i, d in enumerate(layer.data):
    d.radius = R[i]; d.use_root = (i == IDX["pelvis"])
ss = body.modifiers.new("Subsurf", 'SUBSURF'); ss.levels = 2; ss.render_levels = 2
for m in ("Skin", "Subsurf"): bpy.ops.object.modifier_apply(modifier=m)
bpy.ops.object.shade_smooth()
skin_mat = bpy.data.materials.new("Skin"); skin_mat.diffuse_color = (0.86, 0.66, 0.55, 1)
body.data.materials.append(skin_mat)
print("corpo:", len(body.data.vertices), "vertices")

# ---------------------------------------------------------------- rosto e cabelo
parts = []
def prim(kind, name, loc, scale, color, **kw):
    if kind == 'sphere': bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=loc)
    else: bpy.ops.mesh.primitive_cone_add(vertices=20, location=loc, **kw)
    o = bpy.context.object; o.name = name; o.scale = scale
    bpy.ops.object.transform_apply(scale=True)
    m = bpy.data.materials.new(name); m.diffuse_color = color; o.data.materials.append(m)
    bpy.ops.object.shade_smooth(); parts.append(o); return o
for s, x in (("L", 1), ("R", -1)):
    prim('sphere', f"eye.{s}", (0.036*x, -0.092, 1.632), (0.012, 0.010, 0.012), (0.05, 0.04, 0.05, 1))
prim('sphere', "nose", (0, -0.100, 1.600), (0.011, 0.020, 0.016), (0.84, 0.64, 0.53, 1))
prim('sphere', "lips", (0, -0.092, 1.568), (0.024, 0.009, 0.007), (0.65, 0.25, 0.28, 1))
hair = prim('sphere', "hair", (0, 0.015, 1.650), (0.100, 0.112, 0.100), (0.25, 0.14, 0.08, 1))
import bmesh
bm = bmesh.new(); bm.from_mesh(hair.data)
bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.co.y < -0.02 and v.co.z < 1.675], context='VERTS')
bm.to_mesh(hair.data); bm.free()
d = Vector((0, 0.07, -0.20))        # rabo de cavalo
prim('cone', "ponytail", Vector((0, 0.115, 1.55)), (1, 1, 1), (0.25, 0.14, 0.08, 1),
     radius1=0.040, radius2=0.012, depth=d.length)
pt = parts[-1]; pt.rotation_mode = 'QUATERNION'
pt.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(Vector((0, 0.35, -0.9)))
bpy.ops.object.select_all(action='DESELECT')
for o in parts: o.select_set(True)
bpy.context.view_layer.objects.active = parts[0]; bpy.ops.object.join()
face = bpy.context.object; face.name = "FaceHair"

# ---------------------------------------------------------------- armature
bpy.ops.object.armature_add(location=(0, 0, 0)); arm = bpy.context.object; arm.name = "Rig"
bpy.ops.object.mode_set(mode='EDIT'); eb = arm.data.edit_bones
for b in list(eb): eb.remove(b)
def bone(name, head, tail, parent=None, connect=False):
    b = eb.new(name); b.head = head; b.tail = tail
    if parent: b.parent = eb[parent]; b.use_connect = connect
bone("pelvis", (0, 0, 0.95), (0, 0, 1.03))
bone("spine", (0, 0, 1.03), (0, 0, 1.22), "pelvis", True)
bone("chest", (0, 0, 1.22), (0, 0, 1.43), "spine", True)
bone("neck", (0, 0, 1.43), (0, 0, 1.52), "chest", True)
bone("head", (0, 0, 1.52), (0, 0, 1.72), "neck", True)
for s, x in (("L", 1), ("R", -1)):
    bone(f"clavicle.{s}", (0, 0, 1.395), (0.17*x, 0, 1.395), "chest")
    bone(f"upperarm.{s}", (0.17*x, 0, 1.395), (0.45*x, 0, 1.395), f"clavicle.{s}", True)
    bone(f"forearm.{s}", (0.45*x, 0, 1.395), (0.69*x, 0, 1.395), f"upperarm.{s}", True)
    bone(f"hand.{s}", (0.69*x, 0, 1.395), (0.775*x, 0, 1.395), f"forearm.{s}", True)
    for i in range(5):
        h, t = FING[f"finger{i}.{s}"]; bone(f"finger{i}.{s}", h, t, f"hand.{s}")
    bone(f"thigh.{s}", (0.09*x, 0, 0.925), (0.09*x, 0, 0.50), "pelvis")
    bone(f"shin.{s}", (0.09*x, 0, 0.50), (0.09*x, 0, 0.085), f"thigh.{s}", True)
    bone(f"foot.{s}", (0.09*x, 0.005, 0.085), (0.092*x, -0.095, 0.03), f"shin.{s}", True)
    bone(f"toe.{s}", (0.092*x, -0.095, 0.03), (0.092*x, -0.17, 0.022), f"foot.{s}", True)
    bone(f"jiggle_breast.{s}", (0.082*x, -0.05, 1.285), (0.084*x, -0.14, 1.280), "chest")
    bone(f"jiggle_glute.{s}", (0.070*x, 0.05, 0.920), (0.070*x, 0.15, 0.905), "pelvis")
bpy.ops.object.mode_set(mode='OBJECT')

# ---------------------------------------------------------------- pesos
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True); arm.select_set(True); bpy.context.view_layer.objects.active = arm
bpy.ops.object.parent_set(type='ARMATURE_AUTO')
assert len(body.vertex_groups) > 0, "pesos automaticos falharam"

def blend_group(vg_name, center, radius):
    """Misturado: no centro 100% no osso de jiggle, nas bordas cai suave e o resto
    dos pesos e reduzido na mesma proporcao (soma continua 1)."""
    vg = body.vertex_groups[vg_name]; c = Vector(center)
    for v in body.data.vertices:
        dist = (v.co - c).length
        if dist >= radius: continue
        w = 1.0 if dist < radius * 0.5 else (radius - dist) / (radius * 0.5)
        for g in v.groups:
            if g.group != vg.index: g.weight *= (1 - w)
        vg.add([v.index], w, 'REPLACE')
for s, x in (("L", 1), ("R", -1)):
    blend_group(f"jiggle_breast.{s}", (0.084*x, -0.095, 1.28), 0.095)
    blend_group(f"jiggle_glute.{s}", (0.070*x, 0.100, 0.910), 0.125)
bpy.context.view_layer.objects.active = body
bpy.ops.object.vertex_group_limit_total(group_select_mode='ALL', limit=4)
bpy.ops.object.vertex_group_normalize_all(group_select_mode='ALL', lock_active=False)

# rosto/cabelo seguem o osso da cabeca
vg = face.vertex_groups.new(name="head"); vg.add(list(range(len(face.data.vertices))), 1.0, 'REPLACE')
face.parent = arm; face.modifiers.new("Armature", 'ARMATURE').object = arm

# ---------------------------------------------------------------- salvar
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "character_model.blend"))
bpy.ops.export_scene.gltf(filepath=os.path.join(HERE, "character_model.glb"), export_format='GLB')
print("OK")
