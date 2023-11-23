#!/bin/bash
set -e

# Copiar scripts Python para o diretório de trabalho do Jupyter
cd /home/jovyan/work/scripts/
pip install --upgrade pip
pip install -r requirements.txt

# Executar script Python no contêiner Spark
python /home/jovyan/work/scripts/gerar_dados.py
python /home/jovyan/work/scripts/movimento_flat.py