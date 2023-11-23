#!/bin/bash
set -e

# Executar script SQL no MySQL
mysql -h localhost -u root -proot123 -P 3309 sicoop_bd < /home/jovyan/work/data/gerar_tabelas_bd.sql