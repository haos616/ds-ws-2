FROM python:3.5.3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
ADD ./api/requirements /code/requirements

RUN pip install -r /code/requirements/dev.txt

WORKDIR /code
