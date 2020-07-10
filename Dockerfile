FROM python:3.7
MAINTAINER bistroEda test

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN adduser -D user
USER user

