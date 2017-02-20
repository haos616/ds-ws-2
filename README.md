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

```bash
$ docker-compose up
Creating network "ws2_default" with the default driver
Creating volume "ws2_postgres_data" with default driver
Creating ws2_postgres_1
Creating ws2_django_1
Attaching to ws2_postgres_1, ws2_django_1
postgres_1  | The files belonging to this database system will be owned by user "postgres".
postgres_1  | This user must also own the server process.
django_1    | Waiting creating postgres database
postgres_1  | 
postgres_1  | The database cluster will be initialized with locale "en_US.utf8".
postgres_1  | The default database encoding has accordingly been set to "UTF8".
postgres_1  | The default text search configuration will be set to "english".
postgres_1  | 
postgres_1  | Data page checksums are disabled.
postgres_1  | 
postgres_1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
postgres_1  | creating subdirectories ... ok
postgres_1  | selecting default max_connections ... 100
postgres_1  | selecting default shared_buffers ... 128MB
postgres_1  | selecting dynamic shared memory implementation ... posix
postgres_1  | creating configuration files ... ok
postgres_1  | running bootstrap script ... ok
postgres_1  | performing post-bootstrap initialization ... ok
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
postgres_1  | syncing data to disk ... ok
postgres_1  | 
postgres_1  | Success. You can now start the database server using:
postgres_1  | 
postgres_1  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
postgres_1  | 
postgres_1  | 
postgres_1  | WARNING: enabling "trust" authentication for local connections
postgres_1  | You can change this by editing pg_hba.conf or using the option -A, or
postgres_1  | --auth-local and --auth-host, the next time you run initdb.
postgres_1  | waiting for server to start....LOG:  database system was shut down at 2017-02-19 09:39:11 UTC
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
postgres_1  | LOG:  MultiXact member wraparound protections are now enabled
postgres_1  | LOG:  database system is ready to accept connections
postgres_1  | LOG:  autovacuum launcher started
django_1    | Waiting creating postgres database
postgres_1  |  done
postgres_1  | server started
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
postgres_1  | CREATE DATABASE
postgres_1  | 
postgres_1  | CREATE ROLE
postgres_1  | 
postgres_1  | 
postgres_1  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
postgres_1  | 
postgres_1  | LOG:  received fast shutdown request
postgres_1  | waiting for server to shut down....LOG:  aborting any active transactions
postgres_1  | LOG:  autovacuum launcher shutting down
postgres_1  | LOG:  shutting down
postgres_1  | LOG:  database system is shut down
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Waiting creating postgres database
postgres_1  |  done
postgres_1  | server stopped
postgres_1  | 
postgres_1  | PostgreSQL init process complete; ready for start up.
postgres_1  | 
postgres_1  | LOG:  database system was shut down at 2017-02-19 09:39:24 UTC
postgres_1  | LOG:  MultiXact member wraparound protections are now enabled
postgres_1  | LOG:  database system is ready to accept connections
postgres_1  | LOG:  autovacuum launcher started
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Operations to perform:
django_1    |   Apply all migrations: admin, auth, contenttypes, sessions
django_1    | Running migrations:
django_1    |   Applying contenttypes.0001_initial... OK
django_1    |   Applying auth.0001_initial... OK
django_1    |   Applying admin.0001_initial... OK
django_1    |   Applying admin.0002_logentry_remove_auto_add... OK
django_1    |   Applying contenttypes.0002_remove_content_type_name... OK
django_1    |   Applying auth.0002_alter_permission_name_max_length... OK
django_1    |   Applying auth.0003_alter_user_email_max_length... OK
django_1    |   Applying auth.0004_alter_user_username_opts... OK
django_1    |   Applying auth.0005_alter_user_last_login_null... OK
django_1    |   Applying auth.0006_require_contenttypes_0002... OK
django_1    |   Applying auth.0007_alter_validators_add_error_messages... OK
django_1    |   Applying auth.0008_alter_user_username_max_length... OK
django_1    |   Applying sessions.0001_initial... OK
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | /usr/local/lib/python3.5/site-packages/environ/environ.py:608: UserWarning: /code/ws2/.env doesn't exist - if you're not configuring your environment separately, create one.
django_1    |   "environment separately, create one." % env_file)
django_1    | Performing system checks...
django_1    | 
django_1    | System check identified no issues (0 silenced).
django_1    | February 19, 2017 - 09:39:29
django_1    | Django version 1.10.5, using settings 'ws2.settings'
django_1    | Starting development server at http://0.0.0.0:8000/
django_1    | Quit the server with CONTROL-C.
```

```bash
$ docker-compose -f docker-compose.yml -f backup.yml run --rm postgres_backup
Starting ws2_postgres_1
Creating folders /backups/2017/02/19
Creating backup /backups/2017/02/19/2017-02-19T09:48:55.psql.gz
Successfully created backup /backups/2017/02/19/2017-02-19T09:48:55.psql.gz
```

```bash
$ docker-compose -f docker-compose.yml -f backup.yml run --rm postgres_backup list-backups
Listing dirs
/backups
/backups/2017
/backups/2017/02
/backups/2017/02/19
```

```bash
$ docker-compose -f docker-compose.yml -f backup.yml run --rm postgres_backup list-backups /backups/2017/02/19
Listing available backups
/backups/2017/02/19/2017-02-19T09:48:14.psql.gz
/backups/2017/02/19/2017-02-19T09:48:55.psql.gz
/backups/2017/02/19/2017-02-19T09:49:41.psql.gz
/backups/2017/02/19/2017-02-19T09:49:54.psql.gz
```

```bash
$ docker-compose -f docker-compose.yml -f backup.yml run --rm postgres_backup restore /backups/2017/02/19/2017-02-19T09:48:14.psql.gz
Beginning restore from /backups/2017/02/19/2017-02-19T09:48:14.psql.gz
Deleting old database api_db
Deleted api_db database
Creating new database api_db
Restoring database api_db
```

```bash
$ docker-compose logs -f
```

```bash
django_sshd_1  | user:root container:ws2_django_1 password:docker
```

```bash
$ docker-compose down -v
Removing network ws2_default
WARNING: Network ws2_default not found.
Removing volume ws2_postgres_data
ERROR: Unable to remove volume, volume still in use: remove ws2_postgres_data: volume is in use - [8f4fe1b0e79aee39593716e50000fa76405dbff4d4c8c36a76dec600daedc87c, c13642f253016d24793a121d1f29b8795df76aee9c7c034af43ea3791bd96437, 8ad8f8ab2ca89d203d8747278ae4020a81fcc4c1afec715c503373fc12126f11]
```

Need remove container 8f4fe1b0e79aee39593716e50000fa76405dbff4d4c8c36a76dec600daedc87c