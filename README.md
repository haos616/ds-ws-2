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

```bash
$ docker-compose run django python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
```

```bash
$ docker-compose build postgres
Building postgres
Step 1 : FROM postgres:9.6.2
 ---> ecd991538a0f
Step 2 : ADD backup.sh /usr/local/bin/backup
 ---> Using cache
 ---> 53cec657dcdc
Step 3 : ADD restore.sh /usr/local/bin/restore
 ---> Using cache
 ---> 52347b8359c9
Step 4 : ADD list-backups.sh /usr/local/bin/list-backups
 ---> Using cache
 ---> e1e2aa203f86
Step 5 : RUN chmod +x /usr/local/bin/restore     && chmod +x /usr/local/bin/list-backups     && chmod +x /usr/local/bin/backup
 ---> Using cache
 ---> f66b7b0ac699
Step 6 : VOLUME /backups
 ---> Using cache
 ---> 40181a60a1b2
Successfully built 40181a60a1b2
```

```bash
$ docker-compose down -v
Removing ws2_django_1 ... done
Removing ws2_postgres_1 ... done
Removing ws2_django_run_3 ... done
Removing ws2_django_run_2 ... done
Removing ws2_django_run_1 ... done
Removing network ws2_default
Removing volume ws2_postgres_data
```

```
django_1    |     conn = _connect(dsn, connection_factory=connection_factory, async=async)
django_1    | django.db.utils.OperationalError: could not connect to server: Connection refused
django_1    | 	Is the server running on host "postgres" (172.25.0.2) and accepting
django_1    | 	TCP/IP connections on port 5432?
django_1    | 
```

```bash
$ docker-compose down -v
Removing ws2_django_1 ... error
Removing ws2_postgres_1 ... error

ERROR: for ws2_postgres_1  Driver aufs failed to remove root filesystem 8c17aeadbf6c3039be11203995b934148bb0eddb6692185cd66a6bd344276449: rename /var/lib/docker/aufs/mnt/80357318e32fd2137f68b4346a59d5d4b583d755fc6030606920dfaa748bcfdd /var/lib/docker/aufs/mnt/80357318e32fd2137f68b4346a59d5d4b583d755fc6030606920dfaa748bcfdd-removing: device or resource busy

ERROR: for ws2_django_1  Driver aufs failed to remove root filesystem fb40b21494b3332924bd6d5ebb763e303912980b3fca93472b692d964235256c: rename /var/lib/docker/aufs/mnt/139e24f2df5d79ee2cdb1bf3dacb15f3eb08da83be93b273f995ff3bebb3c8b7 /var/lib/docker/aufs/mnt/139e24f2df5d79ee2cdb1bf3dacb15f3eb08da83be93b273f995ff3bebb3c8b7-removing: device or resource busy
Removing network ws2_default
Removing volume ws2_postgres_data
ERROR: Unable to remove volume, volume still in use: remove ws2_postgres_data: volume is in use - [8c17aeadbf6c3039be11203995b934148bb0eddb6692185cd66a6bd344276449]
haos@Dark:~/myprojects/ds-ws-2/ds-ws-2/docker$ /etc/init.d/docker restart
[....] Restarting docker (via systemctl): docker.serviceFailed to restart docker.service: Access denied
 failed!
```

```bash
# service docker restart
```

