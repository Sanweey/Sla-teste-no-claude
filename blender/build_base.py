"""Manequim adulto base: malha procedural + rig + ossos de jiggle + animacao de teste.
Rodar: python build_base.py  (precisa do modulo bpy)"""
import bpy, math, os
from mathutils import Vector

OUT = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.read_factory_settings(use_empty=True)
parts = []

def sphere(name, loc, scale, seg=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=seg, ring_count=seg // 2, location=loc)
    o = bpy.context.object; o.name = name; o.scale = scale
    bpy.ops.object.transform_apply(scale=True); parts.append(o); return o

def limb(name, a, b, ra, rb):
    a, b = Vector(a), Vector(b); d = b - a
    bpy.ops.mesh.primitive_cone_add(vertices=20, radius1=ra, radius2=rb, depth=d.length,
                                    location=(a + b) / 2)
    o = bpy.context.object; o.name = name
    o.rotation_mode = 'QUATERNION'
    o.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(d)
    bpy.ops.object.transform_apply(rotation=True); parts.append(o); return o

# --- corpo (Z para cima, frente = -Y), ~1.70m ---
sphere("head", (0, 0, 1.60), (0.095, 0.11, 0.12))
limb("neck", (0, 0, 1.46), (0, 0, 1.54), 0.05, 0.045)
sphere("chest", (0, 0, 1.30), (0.17, 0.11, 0.17))
limb("waist", (0, 0, 1.00), (0, 0, 1.28), 0.13, 0.15)
sphere("pelvis", (0, 0, 0.97), (0.17, 0.11, 0.11))
for s, x in (("L", 1), ("R", -1)):
    sphere(f"breast.{s}", (0.085 * x, -0.12, 1.30), (0.065, 0.07, 0.065))
    sphere(f"glute.{s}", (0.085 * x, 0.08, 0.93), (0.085, 0.09, 0.10))
    sphere(f"shoulder.{s}", (0.2 * x, 0, 1.40), (0.055, 0.055, 0.055))
    limb(f"upperarm.{s}", (0.2 * x, 0, 1.40), (0.46 * x, 0, 1.40), 0.05, 0.04)
    limb(f"forearm.{s}", (0.46 * x, 0, 1.40), (0.70 * x, 0, 1.40), 0.04, 0.03)
    sphere(f"hand.{s}", (0.76 * x, 0, 1.40), (0.05, 0.03, 0.025))
    limb(f"thigh.{s}", (0.09 * x, 0, 0.92), (0.09 * x, 0, 0.50), 0.085, 0.06)
    limb(f"shin.{s}", (0.09 * x, 0, 0.50), (0.09 * x, 0, 0.08), 0.06, 0.04)
    sphere(f"foot.{s}", (0.09 * x, -0.05, 0.04), (0.045, 0.11, 0.04))

bpy.ops.object.select_all(action='DESELECT')
for o in parts: o.select_set(True)
bpy.context.view_layer.objects.active = parts[0]
bpy.ops.object.join()
body = bpy.context.object; body.name = "Body"
bpy.ops.object.shade_smooth()
mat = bpy.data.materials.new("Skin"); mat.diffuse_color = (0.8, 0.6, 0.5, 1); body.data.materials.append(mat)

# --- armature ---
bpy.ops.object.armature_add(location=(0, 0, 0)); arm = bpy.context.object; arm.name = "Rig"
bpy.ops.object.mode_set(mode='EDIT'); eb = arm.data.edit_bones
for b in list(eb): eb.remove(b)
def bone(name, head, tail, parent=None, connect=False):
    b = eb.new(name); b.head = head; b.tail = tail
    if parent: b.parent = eb[parent]; b.use_connect = connect
    return b
bone("pelvis", (0, 0, 0.95), (0, 0, 1.02))
bone("spine", (0, 0, 1.02), (0, 0, 1.22), "pelvis", True)
bone("chest", (0, 0, 1.22), (0, 0, 1.44), "spine", True)
bone("neck", (0, 0, 1.44), (0, 0, 1.52), "chest", True)
bone("head", (0, 0, 1.52), (0, 0, 1.72), "neck", True)
for s, x in (("L", 1), ("R", -1)):
    bone(f"clavicle.{s}", (0, 0, 1.40), (0.2 * x, 0, 1.40), "chest")
    bone(f"upperarm.{s}", (0.2 * x, 0, 1.40), (0.46 * x, 0, 1.40), f"clavicle.{s}", True)
    bone(f"forearm.{s}", (0.46 * x, 0, 1.40), (0.70 * x, 0, 1.40), f"upperarm.{s}", True)
    bone(f"hand.{s}", (0.70 * x, 0, 1.40), (0.82 * x, 0, 1.40), f"forearm.{s}", True)
    bone(f"thigh.{s}", (0.09 * x, 0, 0.92), (0.09 * x, 0, 0.50), "pelvis")
    bone(f"shin.{s}", (0.09 * x, 0, 0.50), (0.09 * x, 0, 0.08), f"thigh.{s}", True)
    bone(f"foot.{s}", (0.09 * x, 0, 0.08), (0.09 * x, -0.16, 0.03), f"shin.{s}", True)
    # jiggle: peito sai da chest para frente; gluteo sai da pelvis para tras
    bone(f"jiggle_breast.{s}", (0.085 * x, -0.07, 1.30), (0.085 * x, -0.19, 1.30), "chest")
    bone(f"jiggle_glute.{s}", (0.085 * x, 0.04, 0.93), (0.085 * x, 0.17, 0.93), "pelvis")
bpy.ops.object.mode_set(mode='OBJECT')

# --- pesos: automatico, com fallback por grupos de vertices ---
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True); arm.select_set(True); bpy.context.view_layer.objects.active = arm
try:
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    assert len(body.vertex_groups) > 0
except Exception as e:
    print("auto weights falhou:", e)
    body.parent = arm
    body.modifiers.new("Armature", 'ARMATURE').object = arm

# reforca pesos de jiggle (esfera inteira = 1.0 no osso jiggle, borda suave via smooth)
def force_group(vg_name, center, radius):
    vg = body.vertex_groups.get(vg_name) or body.vertex_groups.new(name=vg_name)
    c = Vector(center)
    for v in body.data.vertices:
        d = (v.co - c).length
        if d < radius:
            w = 1.0 if d < radius * 0.6 else (radius - d) / (radius * 0.4)
            for g in v.groups:
                if g.group != vg.index: body.vertex_groups[g.group].remove([v.index])
            vg.add([v.index], w, 'REPLACE')
for s, x in (("L", 1), ("R", -1)):
    force_group(f"jiggle_breast.{s}", (0.085 * x, -0.12, 1.30), 0.075)
    force_group(f"jiggle_glute.{s}", (0.085 * x, 0.08, 0.93), 0.10)

# --- animacao de teste: idle (respiracao + balanco do quadril), loop 48 frames ---
bpy.context.scene.frame_start, bpy.context.scene.frame_end = 1, 48
bpy.context.view_layer.objects.active = arm; bpy.ops.object.mode_set(mode='POSE')
for f, (rz, ry) in {1: (0, 0), 12: (4, -3), 24: (0, 0), 36: (-4, 3), 48: (0, 0)}.items():
    for n, k in (("pelvis", ry), ("chest", rz)):
        pb = arm.pose.bones[n]; pb.rotation_mode = 'XYZ'
        pb.rotation_euler = (0, math.radians(k), math.radians(k * 0.5))
        pb.keyframe_insert("rotation_euler", frame=f)
bpy.ops.object.mode_set(mode='OBJECT')

# --- exporta ---
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "mannequin_base.blend"))
bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, "mannequin_base.glb"), export_format='GLB')

# --- preview ---
sc = bpy.context.scene; sc.render.engine = 'BLENDER_WORKBENCH'
sc.render.resolution_x, sc.render.resolution_y = 600, 800
cam = bpy.data.objects.new("Cam", bpy.data.cameras.new("Cam")); sc.collection.objects.link(cam)
cam.location = (1.2, -3.4, 1.0); cam.rotation_euler = (math.radians(88), 0, math.radians(20)); sc.camera = cam
sc.render.filepath = os.path.join(OUT, "preview.png"); bpy.ops.render.render(write_still=True)
print("OK")
