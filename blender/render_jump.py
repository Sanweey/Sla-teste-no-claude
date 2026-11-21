"""Teste: anima um pulo no quadril, faz bake do jiggle e renderiza frames (Workbench)."""
import bpy, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bake_jiggle
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "jump_frames"); os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE, "mannequin_base.blend"))
a = bpy.data.objects["Rig"]; sc = bpy.context.scene
bpy.context.view_layer.objects.active = a; bpy.ops.object.mode_set(mode='POSE')
for pb in a.pose.bones: pb.location = (0, 0, 0); pb.rotation_euler = (0, 0, 0)
if a.animation_data: a.animation_data_clear()
pb = a.pose.bones["pelvis"]
for f, z in {1: 0, 8: -0.08, 16: 0.25, 24: 0, 32: -0.08, 40: 0.25, 48: 0}.items():
    pb.location = (0, z, 0); pb.keyframe_insert("location", frame=f)
bpy.ops.object.mode_set(mode='OBJECT')
# jiggle exagerado so para este teste (os valores padrao do bake_jiggle.py ficam como estao)
bake_jiggle.SETTINGS["jiggle_breast"] = dict(freq=2.5, damping=0.08, max_offset=0.16)
bake_jiggle.SETTINGS["jiggle_glute"] = dict(freq=3.0, damping=0.10, max_offset=0.14)
bake_jiggle.bake(a)
sc.render.engine = 'BLENDER_WORKBENCH'
sc.render.resolution_x, sc.render.resolution_y = 360, 480
sh = sc.display.shading; sh.light = 'STUDIO'; sh.color_type = 'SINGLE'; sh.single_color = (0.85, 0.65, 0.55)
cd = bpy.data.cameras.new("Cam"); cd.type = 'ORTHO'; cd.ortho_scale = 2.4
cam = bpy.data.objects.new("Cam", cd); sc.collection.objects.link(cam)
cam.location = (4, 0, 1.0); cam.rotation_euler = (math.radians(90), 0, math.radians(90)); sc.camera = cam  # vista lateral
for f in range(1, 49, 2):
    sc.frame_set(f); sc.render.filepath = os.path.join(OUT, f"f{f:02d}.png")
    bpy.ops.render.render(write_still=True)
