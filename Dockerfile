FROM python:3.6

ENV PYTHONUNBUFFERED 1
#RUN mkdir -p /code/app
WORKDIR /code/app
ADD ./requirements.txt /code/app
RUN pip install -r ./requirements.txt

ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait
