```bash
$ cd docker
$ docker-compose build django
Building django
Step 1 : FROM python:3.5.3
3.5.3: Pulling from library/python
5040bd298390: Already exists
fce5728aad85: Already exists
76610ec20bf5: Already exists
9c1bc3c30371: Pull complete
e4b99677d005: Pull complete
639fdf1f74a8: Pull complete
17fa6c425d9b: Pull complete
Digest: sha256:fb303377b7bfa9796d077152ec84e3e9ace396b4d88e2c63d426542cf968a4e9
Status: Downloaded newer image for python:3.5.3
 ---> b0d7fc8a7ace
Step 2 : RUN pip install django==1.10.5
 ---> Running in eb505d6a7efe
Collecting django==1.10.5
  Downloading Django-1.10.5-py2.py3-none-any.whl (6.8MB)
Installing collected packages: django
Successfully installed django-1.10.5
 ---> 784301a9fcd8
Removing intermediate container eb505d6a7efe
Successfully built 784301a9fcd8
```

```bash
$ mkdir api
$ docker-compose run --rm django django-admin startproject ws2 /code
$ id user
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),110(lpadmin),113(scanner),118(bluetooth),999(docker)
$ docker-compose run --rm django chown 1000:1000 /code -R
```
