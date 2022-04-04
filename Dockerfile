
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY src/requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .