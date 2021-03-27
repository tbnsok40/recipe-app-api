# Docker settings 
FROM python:3.7-alpine
MAINTAINER Pyhoo

# unbuffered mode
ENV PYTHONUNBUFFERED 1 

#the reason for this is, it doenst allow python to buffer outputs,
#it just prints directly.
#this avoids some complications and this like that with the docker image when you re running your
#python application.


# copy 'from'  'to'
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


#so it takes the requirements file that we have just copied and it installs it using pip into docker image


#create empty folder in docker
RUN mkdir /app

# switch to basic directory => starting from /app file
WORKDIR /app

COPY ./app /app


RUN adduser -D user
USER user
# switches to the User(me)
# 이건 보안 때문에 하는 것


#DockerFile이 아니라 Dockerfile이다. 소문자 f

