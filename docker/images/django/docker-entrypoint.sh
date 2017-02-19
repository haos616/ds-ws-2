#!/bin/bash
cd /code

if [ "$API_WAIT" ]; then
    while true
    do
        echo 'Waiting creating postgres database'
        sleep 1
        if python manage.py check_db_connection
        then
            break
        fi
    done
fi

if [ "$API_MIGRATE" ]; then
    python manage.py migrate
fi

exec "$@"
