web: gunicorn jobs.wsgi --log-file -
web: python manage.py migrate && gunicorn jobs.wsgi
