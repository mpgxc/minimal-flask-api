FROM python:3.9

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

ADD . /app

RUN apt update -y && \
    apt list --upgradable && \
    apt upgrade -y

COPY ./requirements.txt /app/requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt -U

EXPOSE 8080

CMD ["uwsgi", "app.ini"]
