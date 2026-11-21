"""Pulo completo no manequim: agacha, impulso, ar, aterrissagem, braços, coluna,
com pes plantados no chao. Faz bake do jiggle, salva .blend e renderiza GIFs.
Rodar: xvfb-run -a python render_jump.py   (modulo bpy)"""
import bpy, math, os, sys
from mathutils import Matrix, Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bake_jiggle
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "jump_frames"); os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE, "mannequin_base.blend"))
a = bpy.data.objects["Rig"]; sc = bpy.context.scene
if a.animation_data: a.animation_data_clear()
bpy.context.view_layer.objects.active = a; bpy.ops.object.mode_set(mode='POSE')
P = a.pose.bones
for pb in P: pb.rotation_mode = 'QUATERNION'

def upd(): bpy.context.view_layer.update()
def rot(name, axis, deg):
    """Gira o osso em torno da cabeca, em eixos do mundo (X=lado, Y=tras, Z=cima)."""
    pb = P[name]; h = pb.head.copy()
    T = Matrix.Translation(h)
    pb.matrix = T @ Matrix.Rotation(math.radians(deg), 4, axis) @ T.inverted() @ pb.matrix
    upd()

L = 0.42  # comprimento coxa/canela
def pose(rise, knee, lean, arm_down, arm_back):
    """rise = quanto o quadril sobe (m) alem do que o joelho ja abaixa; knee = flexao em graus."""
    for pb in P: pb.location = (0, 0, 0); pb.rotation_quaternion = (1, 0, 0, 0)
    upd()
    drop = 2 * L * (1 - math.cos(math.radians(knee)))
    pb = P["pelvis"]; pb.matrix = Matrix.Translation((0, 0, rise - drop)) @ pb.matrix; upd()
    rot("spine", 'X', -lean * 0.5); rot("chest", 'X', -lean * 0.5)
    rot("neck", 'X', lean * 0.4); rot("head", 'X', lean * 0.4)
    for s, sg in (("L", 1), ("R", -1)):
        rot(f"upperarm.{s}", 'Y', sg * arm_down)         # abaixa o braco da T-pose
        rot(f"upperarm.{s}", 'X', arm_back)               # balanca pra tras/frente
        rot(f"forearm.{s}", 'X', -20)                     # cotovelo levemente dobrado
        rot(f"thigh.{s}", 'X', -knee)                     # joelho vai pra frente (-Y)
        rot(f"shin.{s}", 'X', knee * 2)                   # canela volta
        rot(f"foot.{s}", 'X', -knee)                      # pe fica reto

# frame: (rise, knee, lean, arm_down, arm_back)
KEYS = {1:  (0.00, 5, 0, 75, 0),
        10: (0.00, 42, 22, 85, 40),     # agacha, bracos pra tras
        17: (0.30, 0, -5, 15, -30),     # impulso, bracos sobem
        24: (0.42, 22, 5, 25, -15),     # apice, joelhos recolhem
        31: (0.25, 5, 0, 50, 0),        # descendo
        37: (0.00, 38, 18, 80, 30),     # aterrissa, absorve
        43: (0.00, 14, 6, 75, 10),      # levanta
        48: (0.00, 5, 0, 75, 0)}
for f, args in KEYS.items():
    sc.frame_set(f); pose(*args)
    for pb in P:
        pb.keyframe_insert("rotation_quaternion", frame=f); pb.keyframe_insert("location", frame=f)
bpy.ops.object.mode_set(mode='OBJECT')
sc.frame_start, sc.frame_end = 1, 48

# jiggle exagerado so para este teste
bake_jiggle.SETTINGS["jiggle_breast"] = dict(freq=2.0, damping=0.04, max_offset=0.28)
bake_jiggle.SETTINGS["jiggle_glute"] = dict(freq=2.3, damping=0.05, max_offset=0.24)
bake_jiggle.bake(a)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "jump_animation.blend"))

# chao + render
bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, -0.005))
sc.render.engine = 'BLENDER_WORKBENCH'; sc.render.resolution_x, sc.render.resolution_y = 360, 480
sh = sc.display.shading; sh.light = 'STUDIO'; sh.color_type = 'OBJECT'
body = bpy.data.objects["Body"]; body.color = (0.85, 0.65, 0.55, 1)
bpy.data.objects["Plane"].color = (0.35, 0.4, 0.45, 1)
def mkcam(name, loc, target, scale):
    cd = bpy.data.cameras.new(name); cd.type = 'ORTHO'; cd.ortho_scale = scale
    c = bpy.data.objects.new(name, cd); sc.collection.objects.link(c)
    c.location = loc
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); return c
cams = {"side": mkcam("side", (5, 0, 1.2), (0, 0, 1.2), 3.0),
        "front": mkcam("front", (3.0, -4.5, 2.0), (0, 0, 1.2), 3.0)}
for name, cam in cams.items():
    sc.camera = cam
    for f in range(1, 49):
        sc.frame_set(f); sc.render.filepath = os.path.join(OUT, f"{name}_{f:02d}.png")
        bpy.ops.render.render(write_still=True)
