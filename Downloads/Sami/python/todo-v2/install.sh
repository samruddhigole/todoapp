#!/bin/bash

#Script for installing dependencies

#if [ ${USER} != "root" ]; then
#    echo "Must be run with root privileges"
#    exit 1
#fi

#Installing python3 and postgres server
#apt update
#apt install -y python3 python3-pip postgresql postgresql-contrib sudo
#sudo service postgresql restart
#Installing python dependencies
#pip3 install -r requirement.txt

#Creating db user and user database for todo app.
sudo -u postgres createuser todouser -s
sudo -u postgres createdb todouser


#Creating linux user for todo app
echo "TODO\n\n\n\n\n\n" | adduser todouser --quiet --disabled-password

#Installing expect for setting linux password via CLI
#apt install -y expect
./reset.expect todouser "admin123" #for security pass this password via env var in future`
#Setting database user password
sudo -u postgres psql -c "ALTER USER todouser PASSWORD 'admin123';"

#Creating todo app database
sudo -u todouser psql -c "create database todo;"

