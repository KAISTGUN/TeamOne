#!/bin/bash
python3 gen_root_pw.py
root_password=$(cat ./root.pw)
export DEBIAN_FRONTEND="noninteractive"
echo PURGE | debconf-communicate mysql-server
echo PURGE | debconf-communicate mysql-server-5.5
echo "mysql-server mysql-server/root_password password ${root_password}" | debconf-set-selections
echo "mysql-server mysql-server/root_password_again password ${root_password}" | debconf-set-selections
apt-get -y install mysql-server
pip3 install PyMySQL
service mysql start
mysql -uroot -p${root_password} < create_bankdb.sql
./get_pubkey.sh
python3 reg_pubkey.py
python3 reg_admin.py
echo PURGE | debconf-communicate mysql-server
echo PURGE | debconf-communicate mysql-server-5.5
