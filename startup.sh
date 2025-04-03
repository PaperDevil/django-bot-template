kill -9 gunicorn
gunicorn project.wsgi:application --workers 1 --bind 0.0.0.0:6261 --daemon