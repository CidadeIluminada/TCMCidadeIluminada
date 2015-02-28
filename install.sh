sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install -y oracle-java8-installer python-dev git python-pip postgresql postgresql-contrib pgadmin3 vim lib32ncurses5-dev lib32stc++6 postgresql-server-dev-9.3
sudo pip install --upgrade pip virtualenvwrapper
sudo mkdir ~/.virtualenvs
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
mkvirtualenv cidadeiluminada
