FROM python:2.7-slim-stretch

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && \
    apt-get install -y ruby ruby-dev ruby-ffi gcc make jpegoptim optipng && \
    gem install sass -N --version="3.4.7" && \
    gem install compass -N --version="1.0.1" && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

VOLUME /blog
WORKDIR /blog
