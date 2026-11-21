"""Pulo completo no manequim: agacha, impulso, ar, aterrissagem, braços, coluna,
com pes plantados no chao. Faz bake do jiggle, salva .blend e renderiza GIFs.
Rodar: xvfb-run -a python render_jump.py   (modulo bpy)"""
import bpy, math, os, sys
from mathutils import Matrix, Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bake_jiggle
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "jump_frames"); os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE, "character_model.blend"))
a = bpy.data.objects["Rig"]; sc = bpy.context.scene
if a.animation_data: a.animation_data_clear()
bpy.context.view_layer.objects.active = a; bpy.ops.object.mode_set(mode='POSE')
P = a.pose.bones
for pb in P: pb.rotation_mode = 'QUATERNION'

L = 0.42  # comprimento coxa/canela
def upd(): bpy.context.view_layer.update()
def rot(name, axis, deg):
    """Gira o osso em torno da cabeca, em eixos do mundo (X=lado, Y=tras, Z=cima)."""
    pb = P[name]; h = pb.head.copy()
    T = Matrix.Translation(h)
    pb.matrix = T @ Matrix.Rotation(math.radians(deg), 4, axis) @ T.inverted() @ pb.matrix
    upd()

ARM = ("clavicle", "upperarm", "forearm", "hand")
LAG = {"L": 2, "R": 3}          # bracos atrasam em relacao ao corpo (overlap)
SIDE_AMP = {"L": 1.0, "R": 0.88}  # lados levemente diferentes, pra nao ficar robotico

def pose(rise, knee, lean, abd, swing, elbow):
    """rise = subida do quadril (m); knee/lean em graus;
    abd = abertura do braco pro lado a partir de pendurado; swing = balanco no plano
    frente/tras (negativo = pra frente e pra cima, positivo = pra tras); elbow = flexao."""
    for pb in P: pb.location = (0, 0, 0); pb.rotation_quaternion = (1, 0, 0, 0)
    upd()
    drop = 2 * L * (1 - math.cos(math.radians(knee)))
    pb = P["pelvis"]; pb.matrix = Matrix.Translation((0, 0, rise - drop)) @ pb.matrix; upd()
    rot("spine", 'X', -lean * 0.5); rot("chest", 'X', -lean * 0.5)
    rot("neck", 'X', lean * 0.4); rot("head", 'X', lean * 0.4)
    for s, sg in (("L", 1), ("R", -1)):
        amp = SIDE_AMP[s]
        sw, ab = swing * amp, abd * (1.1 if s == "R" else 1.0)
        raise_ = max(0, -sw) / 140                       # 0..1 quanto o braco sobe
        rot(f"clavicle.{s}", 'Y', -sg * raise_ * 14)     # ombro sobe junto
        rot(f"upperarm.{s}", 'Y', sg * (88 - ab))        # T-pose -> braco pendurado
        rot(f"upperarm.{s}", 'X', sw)                    # balanco frente/tras
        rot(f"forearm.{s}", 'X', -(elbow + 8 * raise_) * amp)
        rot(f"thigh.{s}", 'X', -knee)
        rot(f"shin.{s}", 'X', knee * 2)
        rot(f"foot.{s}", 'X', -knee)

# frame: (rise, knee, lean, abd, swing, elbow)
KEYS = {1:  (0.00, 5, 0, 12, 5, 15),
        10: (0.00, 42, 22, 10, 55, 25),     # agacha, bracos balancam pra tras
        17: (0.30, 0, -5, 25, -140, 10),    # impulso: bracos sobem pra frente
        24: (0.42, 22, 5, 55, -95, 20),     # apice: bracos abertos
        31: (0.25, 5, 0, 40, -50, 20),      # descendo
        37: (0.00, 38, 18, 20, -30, 35),    # aterrissa, bracos pra equilibrio
        43: (0.00, 14, 6, 12, 15, 20),      # levanta
        48: (0.00, 5, 0, 12, 5, 15)}
for f, args in KEYS.items():
    sc.frame_set(f); pose(*args)
    for pb in P:
        base = pb.name.split(".")[0]
        if base in ARM:
            side = pb.name.split(".")[1]
            fr = f if f == 1 else min(f + LAG[side], 48)
        else:
            fr = f
        pb.keyframe_insert("rotation_quaternion", frame=fr); pb.keyframe_insert("location", frame=fr)
bpy.ops.object.mode_set(mode='OBJECT')
sc.frame_start, sc.frame_end = 1, 48

# jiggle exagerado so para este teste
bake_jiggle.SETTINGS["jiggle_breast"] = dict(freq=2.0, damping=0.04, max_offset=0.28)
bake_jiggle.SETTINGS["jiggle_glute"] = dict(freq=2.3, damping=0.05, max_offset=0.24)
bake_jiggle.bake(a)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "char_jump_animation.blend"))

# chao + render
bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, -0.005))
sc.render.engine = 'BLENDER_WORKBENCH'; sc.render.resolution_x, sc.render.resolution_y = 360, 480
sh = sc.display.shading; sh.light = 'STUDIO'; sh.color_type = 'MATERIAL'
pm = bpy.data.materials.new("floor"); pm.diffuse_color = (0.35, 0.4, 0.45, 1)
bpy.data.objects["Plane"].data.materials.append(pm)
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
