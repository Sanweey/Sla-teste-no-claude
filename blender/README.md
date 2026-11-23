# Personagem 3D: como retomar

Tudo o que foi feito esta nesta pasta. Os arquivos grandes de dados (MakeHuman) e o
Blender como modulo Python **nao** ficam no repositorio; os passos abaixo recriam o ambiente.

## Estado atual

- **Personagem principal:** `mh_character.blend` / `mh_character.glb`
  - Base MakeHuman com morphs (mulher, 25 anos, 1,64 m, busto e gluteos maiores)
  - Pele 2048 px com shader fotorrealista, olhos "molhados", sobrancelhas, cilios, dentes
  - Cabelo de fios (30 mil curvas) + cabelo de placas escondido (para jogo)
  - Biquini (objeto separado) que se mantem por fora do corpo
  - Rig MakeHuman (165 ossos) + ossos de jiggle (`jiggle_breast.*`, `jiggle_glute.*`)
- **Pose natural** (contrapposto): aplicada na hora do render, por `poses.py`.
  O `.blend` fica em pose de repouso (bracos em "A").
- Renders mais recentes: `mh_character_views.png`, `mh_character_face.png`

## Arquivos

| Arquivo | O que faz |
|---|---|
| `fetch_makehuman_data.sh` | Baixa os dados do MakeHuman (PyPI + npm) para `/tmp/mh` |
| `build_mh_character.py` | Monta a personagem. Medidas no topo: `MACRO`, `BREAST`, `EXTRA` |
| `build_hair.py` | Gera o cabelo de fios. Cor: `MELANIN`, `REDNESS` |
| `poses.py` | Poses (hoje: `natural`) |
| `render_mh.py` | Render Cycles: vistas `frente tres_quartos lado costas rosto maos` |
| `bake_jiggle.py` | Grava balanco (mola) nos ossos `jiggle_*` como keyframes |
| `build_character.py`, `build_base.py`, `render_jump.py` | Versoes antigas (modelo procedural e teste de pulo) |

## Recriar o ambiente (Linux)

```bash
# 1. Blender como modulo Python + Pillow
python3 -m venv /tmp/bpyenv
/tmp/bpyenv/bin/pip install bpy pillow

# 2. Bibliotecas graficas para renderizar sem tela
apt-get install -y xvfb libegl1 libgl1 libxrender1 libxi6 libxkbcommon0 libsm6 libxfixes3

# 3. Dados do MakeHuman (~230 MB, fora do repositorio)
bash blender/fetch_makehuman_data.sh /tmp/mh
```

## Gerar e renderizar

```bash
cd blender
xvfb-run -a /tmp/bpyenv/bin/python build_mh_character.py   # corpo, roupa, rig
xvfb-run -a /tmp/bpyenv/bin/python build_hair.py            # cabelo de fios
xvfb-run -a /tmp/bpyenv/bin/python render_mh.py 128         # todas as vistas -> /tmp/mh_*.png
xvfb-run -a /tmp/bpyenv/bin/python render_mh.py rosto 32    # so o rosto, rapido
POSE=a xvfb-run -a /tmp/bpyenv/bin/python render_mh.py 64   # pose em "A"
```

Sempre rode `build_hair.py` depois de `build_mh_character.py` (o cabelo e gerado a partir do arquivo).

## Licenca

Assets do MakeHuman e texturas do `ara3d-data`: CC0 (dominio publico), liberados pelos
autores do MakeHuman em 2020. Ver `LICENSE.txt` dentro do pacote `ara3d-data`.

## Pendencias conhecidas

- Cabelo de fios e rigido (sem fisica) e nao exporta para glTF (no jogo, usar o de placas)
- Pele sem mapas de normal/rugosidade escaneados (relevo e procedural)
- Biquini com aspecto de plastico liso
- Pose fica so no render; nao ha `.blend` ja posado
