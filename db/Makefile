all: mysql

mysql:
	apt-get update
	apt-get -y install python3-pip
	./setup_mysql.sh
	pip3 install tabulate

.PHONY: all mysql

