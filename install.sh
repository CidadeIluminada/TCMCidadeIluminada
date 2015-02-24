sudo apt-get install -y python-dev git python-pip postgresql postgresql-contrib pgadmin3 vim
sudo pip install --upgrade pip virtualenvwrapper
mkdir ~/.virtualenvs
export WORKON_HOME=~/.virtualenvs
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
mkvirtualenv cidadeiluminada
