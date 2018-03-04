FROM python:3.6
MAINTAINER Ravi RT Merugu <rrmerugu@gmail.com>
ENV PYTHONUNBUFFERED 1

ARG build_env
ENV BUILD_ENV ${build_env}

RUN [ -d /webapp ] || mkdir /webapp;
COPY  ./ /webapp
WORKDIR /webapp
RUN pip install --no-cache-dir -r  requirements.txt
#RUN python manage.py migrate
#
#EXPOSE 8000
#CMD python manage.py runserver