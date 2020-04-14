########
# LINT #
########

FROM python:3.8.0-alpine

WORKDIR /usr/src/web_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install flake8
COPY . .

RUN flake8 --ignore=E501,F401,W293 .
