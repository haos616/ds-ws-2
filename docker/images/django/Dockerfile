FROM python:3.5.3

LABEL maintainer Djangostars "info@djangostars.com"

ENV PYTHONUNBUFFERED 1

ADD ./docker/images/django/docker-entrypoint.sh /scripts/docker-entrypoint.sh
ADD ./docker/images/wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

RUN mkdir /code
ADD ./api/requirements /code/requirements

RUN pip install -r /code/requirements/dev.txt

WORKDIR /code

ENTRYPOINT ["/scripts/docker-entrypoint.sh"]
