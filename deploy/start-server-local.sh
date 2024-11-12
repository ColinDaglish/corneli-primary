#!/bin/sh

set -o errexit
set -o nounset

cd /usr/src/app

python manage.py collectstatic --noinput
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000