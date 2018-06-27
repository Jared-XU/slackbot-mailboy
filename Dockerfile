FROM ubuntu:16.04

LABEL maintainer="jared.xu.ncr@gmail.com"

ARG token

ENV SLACKBOT_TOKEN=token 


RUN useradd -m --uid 1001 --gid 0 connections-user

WORKDIR /app

RUN chown -R 1001:0 /app
RUN chmod -R g+rw /app
RUN chmod -R g+x /app
RUN chmod -R g+rw /home/connections-user

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt


RUN pip install -r requirements.txt

COPY . /app

USER 1001

CMD [ "python","server_msg_wait.py" ]
