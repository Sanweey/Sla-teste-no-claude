"""Bake de jiggle (mola + amortecimento) nos ossos 'jiggle_*' como keyframes.

Dentro do Blender: selecione a armature, abra na aba Scripting e rode (Alt+P).
Por linha de comando: python bake_jiggle.py entrada.blend saida.blend
Anime o corpo primeiro, depois rode o bake. Rodar de novo refaz o bake.
"""
import bpy, sys, math
from mathutils import Matrix, Vector

# ---------------- AJUSTES ----------------
# freq: oscilacoes por segundo (maior = mais rigido)
# damping: 0 = balanca pra sempre, 1 = sem balanco (0.15 a 0.5 e o normal)
# max_offset: o quanto a ponta do osso pode se afastar do lugar (metros)
SETTINGS = {
    "jiggle_breast": dict(freq=3.5, damping=0.18, max_offset=0.06),
    "jiggle_glute":  dict(freq=4.5, damping=0.30, max_offset=0.05),
}
SUBSTEPS = 8
# -----------------------------------------

def cfg_for(name):
    for prefix, c in SETTINGS.items():
        if name.startswith(prefix):
            return c

def bake(arm):
    sc = bpy.context.scene
    dt = 1.0 / (sc.render.fps / sc.render.fps_base) / SUBSTEPS
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    bones = [pb for pb in arm.pose.bones if cfg_for(pb.name)]
    if not bones:
        print("Nenhum osso jiggle_* encontrado."); return
    for pb in bones:
        pb.rotation_mode = 'QUATERNION'
    ad = arm.animation_data
    if ad and ad.action:
        for fc in list(ad.action.fcurves) if hasattr(ad.action, "fcurves") else []:
            if any(fc.data_path.startswith(f'pose.bones["{pb.name}"]') for pb in bones):
                ad.action.fcurves.remove(fc)
    state = {}
    frames = range(sc.frame_start, sc.frame_end + 1)
    for pass_no in (0, 1):            # passada 0 = aquecimento (faz o loop fechar bem)
        for f in frames:
            sc.frame_set(f)
            for pb in bones:
                c = cfg_for(pb.name)
                pb.rotation_quaternion = (1, 0, 0, 0)
                bpy.context.view_layer.update()
                head, target, length = pb.head.copy(), pb.tail.copy(), pb.length
                p, v = state.get(pb.name, (target.copy(), Vector()))
                w = 2 * math.pi * c["freq"]; k = w * w; d = 2 * c["damping"] * w
                for _ in range(SUBSTEPS):
                    v += (k * (target - p) - d * v) * dt
                    p += v * dt
                off = p - target
                if off.length > c["max_offset"]:
                    p = target + off.normalized() * c["max_offset"]
                    v *= 0.5
                state[pb.name] = (p, v)
                want = (p - head).normalized()
                cur = (pb.tail - pb.head).normalized()
                q = cur.rotation_difference(want)
                T = Matrix.Translation(head)
                pb.matrix = T @ q.to_matrix().to_4x4() @ T.inverted() @ pb.matrix
                bpy.context.view_layer.update()
                if pass_no == 1:
                    pb.keyframe_insert("rotation_quaternion", frame=f)
    bpy.ops.object.mode_set(mode='OBJECT')
    print(f"Jiggle gravado em {len(bones)} ossos, frames {frames.start}-{frames.stop - 1}")

if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    if len(argv) >= 2 and argv[0].endswith(".blend"):
        bpy.ops.wm.open_mainfile(filepath=argv[0])
    arm = bpy.context.active_object
    if not arm or arm.type != 'ARMATURE':
        arm = next(o for o in bpy.data.objects if o.type == 'ARMATURE')
    bake(arm)
    if len(argv) >= 2 and argv[0].endswith(".blend"):
        bpy.ops.wm.save_as_mainfile(filepath=argv[1])
