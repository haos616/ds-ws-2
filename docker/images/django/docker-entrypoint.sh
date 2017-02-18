#!/bin/bash
cd /code

if [ "$API_MIGRATE" ]; then
    python manage.py migrate
fi

exec "$@"
