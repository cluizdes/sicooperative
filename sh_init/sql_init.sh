#!/bin/bash
set -e

cp /home/jovyan/work/data/mysqld.sock /var/run/mysqld/.

chmod 777 -R /var/run/mysqld
chmod 777 -R /var/lib/mysql

mysql_upgrade -uroot -proot123

service mysql restart

# Executar script SQL no MySQL
mysql -h mysql -usicoop -psicoop -P 3306 sicoop_bd < /home/jovyan/work/data/gerar_tabelas_bd.sql