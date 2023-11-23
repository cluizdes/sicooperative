#!/bin/bash
set -e

# Copiar scripts Python para o diretório de trabalho do Jupyter
cd /home/jovyan/work/spark_script/
pip install --upgrade pip
pip install -r requirements.txt

# Executar script Python no contêiner Spark
python /home/jovyan/work/spark_script/gerar_dados.py
python /home/jovyan/work/spark_script/movimento_flat.py