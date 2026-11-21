"""Renderiza o modelo em 4 vistas (T-pose) + 1 pose de teste de deformacao."""
import bpy, math, os
from mathutils import Matrix, Vector
HERE = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE, "character_model.blend"))
sc = bpy.context.scene; a = bpy.data.objects["Rig"]; P = a.pose.bones
sc.render.engine = 'BLENDER_WORKBENCH'; sc.render.resolution_x = sc.render.resolution_y = 600
sh = sc.display.shading; sh.light = 'STUDIO'; sh.color_type = 'MATERIAL'
sh.show_cavity = True; sh.cavity_type = 'BOTH'
sc.render.film_transparent = False
w = bpy.data.worlds.new("w"); w.color = (0.18, 0.2, 0.23); sc.world = w
def cam(name, loc, target, scale):
    cd = bpy.data.cameras.new(name); cd.type = 'ORTHO'; cd.ortho_scale = scale
    c = bpy.data.objects.new(name, cd); sc.collection.objects.link(c); c.location = loc
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); return c
views = {"frente": (0, -5, 0.88), "lado": (5, 0, 0.88), "costas": (0, 5, 0.88), "tres_quartos": (3.2, -3.8, 1.4)}
def shoot(prefix, scale):
    for n, loc in views.items():
        sc.camera = cam(n, loc, (0, 0, 0.88), scale); sc.render.filepath = f"/tmp/{prefix}_{n}.png"
        bpy.ops.render.render(write_still=True)
shoot("view", 2.0)
# pose de teste: braços pra cima, joelhos dobrados, tronco inclinado
bpy.context.view_layer.objects.active = a; bpy.ops.object.mode_set(mode='POSE')
def rot(name, axis, deg):
    pb = P[name]; h = pb.head.copy(); T = Matrix.Translation(h)
    pb.matrix = T @ Matrix.Rotation(math.radians(deg), 4, axis) @ T.inverted() @ pb.matrix
    bpy.context.view_layer.update()
rot("spine", 'X', -12); rot("chest", 'X', -12); rot("head", 'X', 8)
for s, sg in (("L", 1), ("R", -1)):
    rot(f"upperarm.{s}", 'Y', sg * 20); rot(f"upperarm.{s}", 'X', -120); rot(f"forearm.{s}", 'X', -35)
    for i in range(5): rot(f"finger{i}.{s}", 'X', -30)
    rot(f"thigh.{s}", 'X', -45); rot(f"shin.{s}", 'X', 90); rot(f"foot.{s}", 'X', -45)
shoot("pose", 2.0)
