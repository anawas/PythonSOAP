FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get clean \
    && apt-get -y update \
    && pip install --upgrade pip  \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY . /app
EXPOSE 7789
CMD ["python", "server.py"]
