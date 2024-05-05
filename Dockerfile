FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

