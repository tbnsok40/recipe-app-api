# recipe-app-api

> 1. Dockerfile 셍성 \
FROM python:3.7-alpine \
MAINTAINER Pyhoo\
ENV PYTHONUNBUFFERED 1 \
COPY ./requirements.txt /requirements.txt\
RUN pip install -r /requirements.txt\
RUN mkdir /app\
WORKDIR /app\
COPY ./app /app\
RUN adduser -D user\
USER user


> 2. docker-compose.yml
version: '3'\
services:\
  app:\
    build:\
      context: . \
    ports:\
      - '8000:8000'\
    volumes: \
      - ./app:/app\
    command: >\
      sh -c "python manage.py runserver 0.0.0.0:8000"\

> 3. requirements.txt
Django>=2.1.3,<2.2.0
store django in that versions(대소비교 유의)
djangorestframework>=3.9.0,<3.10.0
flake8>=3.6.0,<3.7.0
docker build . >> 이렇게 시작
alpine image is very ligthweight image that runs python


> sh -c : for clear writing, not necessary (shell에 command를 하겠다고 명시적으로 사용
> 4. terminal > docker compose run app sh -c "django-admin.py startproject app" 


>quiz 1
Every time you push a change to GitHub, Travis-CI will automatically detect the push and run out scripts.
\
quiz 2
Django searches for any Python module starting with "test". This is why you can store your tests in "tests.py" or "tests/test_something.py"
\
quiz 3
Correct! Normalizing the email address will ensure that the domain (everything after the "@") is lowercase




since we working on TDD, write out test first and then we're going to implement our model afterwards.
