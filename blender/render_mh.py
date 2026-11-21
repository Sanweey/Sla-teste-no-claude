"""Render Cycles do mh_character.blend em pose relaxada.
Uso: python render_mh.py [frente tres_quartos lado costas rosto] [amostras]   -> /tmp/mh_<vista>.png"""
import bpy, math, os, sys
from mathutils import Matrix, Vector
HERE = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE, "mh_character.blend"))
sc = bpy.context.scene; a = bpy.data.objects["Rig"]; P = a.pose.bones
bpy.context.view_layer.objects.active = a; bpy.ops.object.mode_set(mode='POSE')
def rot(name, axis, deg):
    pb = P[name]; h = pb.head.copy(); T = Matrix.Translation(h)
    pb.matrix = T @ Matrix.Rotation(math.radians(deg), 4, axis) @ T.inverted() @ pb.matrix
    bpy.context.view_layer.update()
ARM_DOWN = float(os.environ.get("ARM_DOWN", 28))
for s, sg in (("L", 1), ("R", -1)):
    rot(f"upperarm01.{s}", 'Y', sg * ARM_DOWN); rot(f"lowerarm01.{s}", 'X', -10)
if os.environ.get("POSE") == "teste":   # pose forcada pra checar deformacao
    rot("spine03", 'X', -15)
    for s, sg in (("L", 1), ("R", -1)):
        rot(f"upperarm01.{s}", 'Y', -sg * (ARM_DOWN + 100)); rot(f"lowerarm01.{s}", 'X', -40)
        rot(f"upperleg01.{s}", 'X', -55); rot(f"lowerleg01.{s}", 'X', 100); rot(f"foot.{s}", 'X', -45)
head_z = (a.matrix_world @ P["head"].head).z
bpy.ops.object.mode_set(mode='OBJECT')

sc.render.engine = 'CYCLES'; cy = sc.cycles; cy.device = 'CPU'
cy.samples = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 64
cy.transparent_max_bounces = 64; cy.max_bounces = 12
try: cy.use_denoising = True
except Exception: pass
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
w = bpy.data.worlds.new("w"); w.use_nodes = True; sc.world = w
bg = w.node_tree.nodes["Background"]; bg.inputs[0].default_value = (0.26, 0.28, 0.31, 1); bg.inputs[1].default_value = 0.7
def light(name, loc, energy, size, target=(0, 0, 1.0), color=(1, 1, 1)):
    d = bpy.data.lights.new(name, 'AREA'); d.energy = energy; d.size = size; d.color = color
    o = bpy.data.objects.new(name, d); sc.collection.objects.link(o); o.location = loc
    o.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
light("key", (2.0, -2.8, 2.6), 230, 1.6, color=(1.0, 0.96, 0.9))
light("fill", (-2.8, -1.6, 1.5), 70, 2.5, color=(0.9, 0.95, 1.0))
light("rim", (0.6, 2.8, 2.4), 200, 1.2)
# chao
bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, 0)); fl = bpy.context.object
fm = bpy.data.materials.new("floor"); fm.use_nodes = True; fm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.08, 0.085, 0.095, 1)
fm.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.8; fl.data.materials.append(fm)
def cam(name, loc, target, lens):
    cd = bpy.data.cameras.new(name); cd.lens = lens
    c = bpy.data.objects.new(name, cd); sc.collection.objects.link(c); c.location = loc
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); return c
mid = head_z * 0.52
views = {"frente": ((0, -5.4, mid + 0.1), (0, 0, mid), 60, (600, 800)),
         "tres_quartos": ((3.4, -4.1, mid + 0.35), (0, 0, mid), 60, (600, 800)),
         "lado": ((5.4, 0, mid + 0.1), (0, 0, mid), 60, (600, 800)),
         "costas": ((0, 5.4, mid + 0.1), (0, 0, mid), 60, (600, 800)),
         "rosto": ((0.45, -1.35, head_z + 0.09), (0, 0, head_z + 0.08), 85, (700, 700))}
only = [v for v in sys.argv if v in views]
for n, (loc, tgt, lens, res) in views.items():
    if only and n not in only: continue
    sc.camera = cam(n, loc, tgt, lens); sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.filepath = f"/tmp/mh_{n}.png"; bpy.ops.render.render(write_still=True)
