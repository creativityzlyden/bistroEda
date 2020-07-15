FROM python:3.7
MAINTAINER babushkin.a.l@yandex.ru

ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

