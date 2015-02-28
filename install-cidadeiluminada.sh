cd webservice
workon cidadeiluminada
pip install -r requirements.txt
pip install -r requirements-dev.txt
python manage.py db upgrade
python manage.py runserver
