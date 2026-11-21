"""Render Cycles do mh_character.blend em pose relaxada.
Uso: python render_mh.py [frente tres_quartos lado costas rosto] [amostras]   -> /tmp/mh_<vista>.png"""
import bpy, math, os, sys
import numpy as np
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
EYE = a.matrix_world @ P["eye.L"].head
bpy.ops.object.mode_set(mode='OBJECT')

sc.render.engine = 'CYCLES'; cy = sc.cycles; cy.device = 'CPU'
cy.samples = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 64
cy.transparent_max_bounces = 64; cy.max_bounces = 12
try: cy.use_denoising = True
except Exception: pass
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
sc.view_settings.exposure = float(os.environ.get("EXPOSURE", -0.75))
w = bpy.data.worlds.new("w"); w.use_nodes = True; sc.world = w
bg = w.node_tree.nodes["Background"]; bg.inputs[0].default_value = (0.2, 0.21, 0.23, 1); bg.inputs[1].default_value = 0.35
def light(name, loc, energy, size, target=(0, 0, 1.0), color=(1, 1, 1)):
    d = bpy.data.lights.new(name, 'AREA'); d.energy = energy; d.size = size; d.color = color
    o = bpy.data.objects.new(name, d); sc.collection.objects.link(o); o.location = loc
    o.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
# estudio fotografico: softbox principal, rebatedor, luz de cabelo e fundo infinito
light("key", (1.6, -2.2, 2.4), 140, 1.6, color=(1.0, 0.95, 0.88))
light("fill", (-2.6, -1.8, 1.0), 18, 3.0, color=(0.92, 0.96, 1.0))
light("hair", (-0.9, 2.2, 2.8), 90, 1.0, color=(1.0, 0.97, 0.95))
light("rim", (1.8, 1.8, 1.6), 90, 0.8)
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, 0)); fl = bpy.context.object
me = fl.data; import bmesh
bm = bmesh.new(); bm.from_mesh(me); bmesh.ops.delete(bm, geom=bm.verts[:], context='VERTS')
prof = [(y, 0.0) for y in np.linspace(-8, 2.5, 30)] + [(2.5 + 1.2 * math.sin(t), 1.2 - 1.2 * math.cos(t)) for t in np.linspace(0.05, math.pi / 2, 12)] + [(3.7, z) for z in np.linspace(1.3, 8, 10)]
rows = []
for x in (-10, 10):
    rows.append([bm.verts.new((x, y, z)) for y, z in prof])
for i in range(len(prof) - 1):
    bm.faces.new((rows[0][i], rows[1][i], rows[1][i + 1], rows[0][i + 1]))
bm.to_mesh(me); bm.free()
for p in me.polygons: p.use_smooth = True
fm = bpy.data.materials.new("backdrop"); fm.use_nodes = True
fb = fm.node_tree.nodes["Principled BSDF"]; fb.inputs["Base Color"].default_value = (0.11, 0.115, 0.125, 1); fb.inputs["Roughness"].default_value = 0.85
me.materials.append(fm)
EYE = a.matrix_world @ P["eye.L"].head
def cam(name, loc, target, lens, fstop):
    cd = bpy.data.cameras.new(name); cd.lens = lens
    cd.dof.use_dof = True; cd.dof.aperture_fstop = fstop
    cd.dof.focus_distance = (Vector(loc) - ((EYE + Vector((0, -0.012, 0))) if name == "rosto" else Vector(target))).length
    c = bpy.data.objects.new(name, cd); sc.collection.objects.link(c); c.location = loc
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); return c
mid = head_z * 0.52
views = {"frente": ((0, -5.4, mid + 0.1), (0, 0, mid), 60, (600, 800), 4.0),
         "tres_quartos": ((3.4, -4.1, mid + 0.35), (0, 0, mid), 60, (600, 800), 4.0),
         "lado": ((5.4, 0, mid + 0.1), (0, 0, mid), 60, (600, 800), 4.0),
         "costas": ((0, 3.3, mid + 0.1), (0, 0, mid), 40, (600, 800), 4.0),
         "rosto": ((0.38, -1.15, head_z + 0.07), (0, 0, head_z + 0.06), 85, (700, 800), 5.6)}
only = [v for v in sys.argv if v in views]
for n, (loc, tgt, lens, res, fstop) in views.items():
    if only and n not in only: continue
    sc.camera = cam(n, loc, tgt, lens, fstop); sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.filepath = f"/tmp/mh_{n}.png"; bpy.ops.render.render(write_still=True)
