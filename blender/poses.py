"""Poses para o rig do MakeHuman (mh_character.blend).
As rotacoes sao em eixos do mundo (X = lado, Y = tras, Z = cima), em torno da cabeca do osso.
Uso: import poses; poses.apply(arm, "natural")"""
import bpy, math
from mathutils import Matrix, Vector, Quaternion


def _rot(arm, name, axis, deg):
    pb = arm.pose.bones[name]; h = pb.head.copy(); T = Matrix.Translation(h)
    pb.matrix = T @ Matrix.Rotation(math.radians(deg), 4, axis) @ T.inverted() @ pb.matrix
    bpy.context.view_layer.update()


def _move(arm, name, offset):
    pb = arm.pose.bones[name]
    pb.matrix = Matrix.Translation(Vector(offset)) @ pb.matrix
    bpy.context.view_layer.update()


def _local(arm, name, axis, deg):
    """Rotacao no eixo local do osso (bom pra dobrar dedos, que tem eixo proprio)."""
    pb = arm.pose.bones[name]; pb.rotation_mode = 'QUATERNION'
    ax = {'X': (1, 0, 0), 'Y': (0, 1, 0), 'Z': (0, 0, 1)}[axis]
    pb.rotation_quaternion = pb.rotation_quaternion @ Quaternion(ax, math.radians(deg))
    bpy.context.view_layer.update()


CURL_SIGN = 1


def _curl_fingers(arm, s, base, extra=0.0):
    """Dedos relaxados: cada falange dobra um pouco mais que a anterior."""
    for f in range(2, 6):
        for k, amt in ((1, 10), (2, 16), (3, 12)):
            _local(arm, f"finger{f}-{k}.{s}", 'X', CURL_SIGN * (amt + base + extra * f))
    _local(arm, f"finger1-2.{s}", 'X', CURL_SIGN * 8); _local(arm, f"finger1-3.{s}", 'X', CURL_SIGN * 10)


def natural(arm):
    global ARM_TWIST
    """Contrapposto: peso na perna direita, quadril inclinado, ombros no sentido oposto."""
    R = lambda n, a, d: _rot(arm, n, a, d)
    # quadril: desloca pro lado da perna de apoio e inclina (lado esquerdo desce)
    _move(arm, "root", (-0.035, 0, 0))
    R("root", 'Y', -5)                       # inclina a bacia
    R("root", 'Z', 6)                        # leve rotacao, corpo em 3/4 sutil
    # perna de apoio (direita): reta e vertical
    R("upperleg01.R", 'Y', 5 - 3)            # compensa a bacia (+5) e fecha um pouco (-3)
    R("foot.R", 'Z', -4)
    # perna livre (esquerda): joelho dobrado, pe pra frente e virado pra fora
    R("upperleg01.L", 'Y', 5 + 6)            # compensa a bacia e traz o pe pra perto do outro
    R("upperleg01.L", 'X', -10); R("upperleg01.L", 'Z', 12)
    R("lowerleg01.L", 'X', 17)
    R("foot.L", 'X', -6)
    # coluna compensa: ombros inclinam ao contrario do quadril
    R("spine04", 'Y', 3); R("spine03", 'Y', 3); R("spine02", 'Y', 2)
    R("spine03", 'Z', -4)                    # tronco gira de volta pra camera
    R("spine02", 'X', 2)
    # cabeca: inclinada e virada levemente
    R("neck02", 'Y', -3); R("head", 'Y', -5); R("head", 'Z', -6); R("head", 'X', 3)
    # bracos soltos, assimetricos
    R("upperarm01.R", 'Y', -37); R("upperarm01.R", 'X', 17)
    R("lowerarm01.R", 'X', -12)
    _local(arm, "lowerarm02.R", 'Y', ARM_TWIST); R("wrist.R", 'Z', -8)
    R("upperarm01.L", 'Y', 39); R("upperarm01.L", 'X', 14)
    R("lowerarm01.L", 'X', -9)
    _local(arm, "lowerarm02.L", 'Y', -ARM_TWIST); R("wrist.L", 'Z', 10)
    _curl_fingers(arm, "R", 12); _curl_fingers(arm, "L", 16, 1.5)


ARM_TWIST = -50   # gira o antebraco: palma virada pra coxa

POSES = {"natural": natural}


def ground(arm, body, foot_names=("foot.R", "foot.L")):
    """Desce/sobe o personagem pra que o ponto mais baixo do corpo toque o chao (z=0)."""
    dg = bpy.context.evaluated_depsgraph_get()
    ev = body.evaluated_get(dg); me = ev.to_mesh()
    zmin = min((ev.matrix_world @ v.co).z for v in me.vertices)
    ev.to_mesh_clear()
    _move(arm, "root", (0, 0, -zmin))


def apply(arm, name):
    POSES[name](arm)
    ground(arm, bpy.data.objects["Body"])
