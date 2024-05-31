FROM python:3-alpine3.10

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN pip install -r /usr/src/app/requirements.txt

# copy project
COPY . /usr/src/app/
