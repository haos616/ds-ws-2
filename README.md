```bash
$ docker-compose config
networks: {}
services:
  django:
    build:
      context: /home/haos/myprojects/ds-ws-2/ds-ws-2
      dockerfile: ./docker/services/django/Dockerfile
    image: hub.haos616.com/ws2/django:dev
    volumes:
    - /home/haos/myprojects/ds-ws-2/ds-ws-2/api:/code:rw
version: '2.0'
volumes: {}
```

```bash
$ cd docker
$ docker-compose build django
Building django
Step 1 : FROM python:3.5.3
 ---> b0d7fc8a7ace
Step 2 : RUN mkdir /code
 ---> Running in 223fdd708b1f
 ---> 915c3167c347
Removing intermediate container 223fdd708b1f
Step 3 : ADD ./api/requirements /code/requirements
 ---> 7780d02e74fc
Removing intermediate container 637e9e08bc07
Step 4 : RUN pip install -r /code/requirements/dev.txt
 ---> Running in d4c6cc020315
Collecting django<1.11,>=1.10 (from -r /code/requirements/base.txt (line 1))
  Downloading Django-1.10.5-py2.py3-none-any.whl (6.8MB)
Installing collected packages: django
Successfully installed django-1.10.5
 ---> 5c269e8cd736
Removing intermediate container d4c6cc020315
Successfully built 5c269e8cd736
```

```bash
$ mkdir api
$ docker-compose run --rm django django-admin startproject ws2 /code
$ id user
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),110(lpadmin),113(scanner),118(bluetooth),999(docker)
$ docker-compose run --rm django chown 1000:1000 /code -R
```

```bash
$ docker-compose up
Recreating ws2_django_1
Attaching to ws2_django_1
django_1  | Performing system checks...
django_1  | 
django_1  | System check identified no issues (0 silenced).
django_1  | 
django_1  | You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
django_1  | Run 'python manage.py migrate' to apply them.
django_1  | February 18, 2017 - 09:32:19
django_1  | Django version 1.10.5, using settings 'ws2.settings'
django_1  | Starting development server at http://0.0.0.0:8000/
django_1  | Quit the server with CONTROL-C.
```
