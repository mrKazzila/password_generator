FROM python:3.11-slim as python

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && apt-get -y upgrade

WORKDIR /app
COPY ./requirements.txt ./pyproject.toml ./

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .
