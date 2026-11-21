"""Render realista (Cycles, CPU) do modelo em pose relaxada: frente, 3/4, lado, costas,
mais um close do rosto. Salva /tmp/cv_*.png"""
import bpy, math, os, sys
from mathutils import Matrix, Vector
HERE = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE, "character_model.blend"))
sc = bpy.context.scene; a = bpy.data.objects["Rig"]; P = a.pose.bones
bpy.context.view_layer.objects.active = a; bpy.ops.object.mode_set(mode='POSE')
def rot(name, axis, deg):
    pb = P[name]; h = pb.head.copy(); T = Matrix.Translation(h)
    pb.matrix = T @ Matrix.Rotation(math.radians(deg), 4, axis) @ T.inverted() @ pb.matrix
    bpy.context.view_layer.update()
for s, sg in (("L", 1), ("R", -1)):                      # pose relaxada
    rot(f"upperarm.{s}", 'Y', sg * 72); rot(f"forearm.{s}", 'X', -12)
    for i in range(5): rot(f"finger{i}.{s}", 'X', -12 - 4*(i % 3))
    rot(f"thigh.{s}", 'Z', sg * -4); rot(f"thigh.{s}", 'X', -10); rot(f"shin.{s}", 'X', 10)
bpy.ops.object.mode_set(mode='OBJECT')

sc.render.engine = 'CYCLES'; cy = sc.cycles; cy.device = 'CPU'
cy.samples = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 40
try: cy.use_denoising = True
except Exception: pass
sc.render.resolution_x, sc.render.resolution_y = 600, 800
w = bpy.data.worlds.new("w"); w.use_nodes = True; sc.world = w
bg = w.node_tree.nodes["Background"]; bg.inputs[0].default_value = (0.30, 0.33, 0.37, 1); bg.inputs[1].default_value = 0.9
def light(name, kind, loc, energy, size):
    d = bpy.data.lights.new(name, kind); d.energy = energy
    if kind == 'AREA': d.size = size
    o = bpy.data.objects.new(name, d); sc.collection.objects.link(o); o.location = loc
    o.rotation_euler = (Vector((0, 0, 0.95)) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); return o
light("key", 'AREA', (2.2, -3.0, 2.6), 170, 2.0)
light("fill", 'AREA', (-3.0, -2.0, 1.4), 55, 2.5)
light("rim", 'AREA', (0.5, 3.0, 2.2), 110, 1.5)
sc.view_settings.view_transform = "Standard"
def cam(name, loc, target, lens):
    cd = bpy.data.cameras.new(name); cd.lens = lens
    c = bpy.data.objects.new(name, cd); sc.collection.objects.link(c); c.location = loc
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); return c
views = {"frente": ((0, -5.2, 0.95), (0, 0, 0.88), 62), "tres_quartos": ((3.6, -3.8, 1.25), (0, 0, 0.88), 62),
         "lado": ((5.2, 0, 0.95), (0, 0, 0.88), 62), "costas": ((0, 5.2, 0.95), (0, 0, 0.88), 62),
         "rosto": ((0.35, -1.5, 1.62), (0, 0, 1.58), 85)}
only = [v for v in sys.argv if v in views]
for n, (loc, tgt, lens) in views.items():
    if only and n not in only: continue
    sc.camera = cam(n, loc, tgt, lens)
    if n == "rosto": sc.render.resolution_x = sc.render.resolution_y = 700
    else: sc.render.resolution_x, sc.render.resolution_y = 600, 800
    sc.render.filepath = f"/tmp/cv_{n}.png"; bpy.ops.render.render(write_still=True)
