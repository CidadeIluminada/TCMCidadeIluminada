cd webservice
workon cidadeiluminada
pip install -r requirements.txt
python manage.py db upgrade
python manage.py runserver
