web: unicorn studio_pitagora.wsgi --log-file -
web: python manage.py runserver && gunicorn studio_pitagora.wsgi  --bind 0.0.0.0:8000