FROM python:3.10-slim

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo "hi there"

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev

# install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/app/

CMD ["gunicorn","main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8008"]
