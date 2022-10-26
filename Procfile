release: sh -c 'python manage.py makemigrations && python manage.py migrate'
web: gunicorn startin.wsgi --log-file -
