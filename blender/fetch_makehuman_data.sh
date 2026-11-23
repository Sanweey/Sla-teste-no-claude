#!/usr/bin/env bash
# Baixa os dados do MakeHuman usados pelo build_mh_character.py
#   - targets.npz (morphs) do pacote "makehuman" no PyPI
#   - texturas em alta (pele 2048px, olhos 1024px) do pacote ara3d-data no npm (CC0)
#   - malha base, esqueleto, pesos, texturas de pele e proxies do pacote "makehuman-data-v1" no npm
# Os arquivos ficam fora do repositorio (sao grandes). Padrao: /tmp/mh
set -euo pipefail
DEST="${1:-/tmp/mh}"
mkdir -p "$DEST/pypi" "$DEST/npm"
cd "$DEST/pypi"
pip download makehuman==1.3.2 --no-deps -d . >/dev/null
python3 -c "import zipfile,glob; zipfile.ZipFile(glob.glob('makehuman-*.whl')[0]).extract('makehuman/data/targets.npz','.')"
cd "$DEST/npm"
curl -sL -o mh.tgz https://registry.npmjs.org/makehuman-data-v1/-/makehuman-data-v1-0.0.2.tgz
tar xzf mh.tgz
mkdir -p "$DEST/ara" && cd "$DEST/ara"
curl -sL -o ara.tgz https://registry.npmjs.org/ara3d-data/-/ara3d-data-1.2.0.tgz
tar xzf ara.tgz package/assets/textures package/assets/LICENSE.txt
echo "MH_TARGETS=$DEST/pypi/makehuman/data/targets.npz"
echo "MH_DATA=$DEST/npm/package/public/data"
echo "ARA_TEX=$DEST/ara/package/assets/textures"
