#!/bin/bash
cd /code

USER_ID=${LOCAL_USER_ID:-1000}

echo "Starting with UID : $USER_ID"
useradd --shell /bin/bash -u $USER_ID -o -c "" -m user
export HOME=/home/user

if [ "$API_WAIT" ]; then
    while true
    do
        echo 'Waiting creating postgres database'
        sleep 1
        if gosu user python manage.py check_db_connection
        then
            break
        fi
    done
fi

if [ "$API_MIGRATE" ]; then
    gosu user python manage.py migrate
fi

gosu user "$@"
