# Docker settings 
FROM python:3.7-alpine
MAINTAINER Pyhoo

ENV PYTHONUNBUFFERED 1 
# unbuffered mode

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app 
#create empty folder in docker
WORKDIR /app 
# switch to basic directory
COPY ./app /app

RUN adduser -D user
USER user
# switches to the User(me)

# 이건 보안 때문에 하는 것

#DockerFile이 아니라 Dockerfile이다. 소문자 f

