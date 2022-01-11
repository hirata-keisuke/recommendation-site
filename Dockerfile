FROM python:3.9.9
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt && mkdir /src
WORKDIR /src
