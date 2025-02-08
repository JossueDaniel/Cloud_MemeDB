FROM python:3.12.9-alpine3.21
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/django_project

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code/