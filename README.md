# TCMCidadeIluminada

## Instaçacao de ambiente no Ubuntu 

- sudo apt-get install python-pip python-dev build-essential git sqlite3
- $ sudo pip install --upgrade pip 
- $ sudo pip install --upgrade virtualenv 
- $ sudo pip install virtualenvwrapper

## Baixando e Instalando aplicacao

- @ http://roundhere.net/journal/virtualenv-ubuntu-12-10/
- inserir . /usr/local/bin/virtualenvwrapper.sh   no fim de ~./bashrc
- $ git clone https://github.com/HardDiskD/TCMCidadeIluminada
- $ cd TCMCidadeIluminada
- $ pip install -r requirement.txt
- $ python manage.py db upgrade
- $ python manage.py runserver


## Rotas da aplicacao
- http://localhost:5000/protocolos
- http://localhost:5000/protocolos/novo
- http://localhost:5000/protocolos/protocolos.json


## Comandos úteis virtualenv

- $ mkvirtualenv myawesomeproject     cria ambiente virtual 
- $ workon myawesomeproject           entra no ambiente virtual

