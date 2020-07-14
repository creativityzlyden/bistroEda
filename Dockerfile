FROM python:3
MAINTAINER babushkin.a.l@yandex.ru

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt


