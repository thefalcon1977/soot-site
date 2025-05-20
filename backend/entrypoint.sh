#!/bin/sh

# if any of the commands in your code fails the entire scripts fails.
set -o errexit

# exit if any of your variables is not set.
set -o nounset

set -x

# Clear Python caches
find . -name "*.pyc" -exec rm -f {} \;

# Django commands
python manage.py makemigrations
# python manage.py migrate --noinput
python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8009
# gunicorn --config config/gunicorn/prod.py kernel.wsgi:application

exec "$@"