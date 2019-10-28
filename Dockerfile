FROM python:alpine

LABEL maintanier="Ahmet Erkoc<aerkoc01@gmail.com>"

COPY code/ /code/

WORKDIR /code

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

RUN python create_tables.py

EXPOSE 5000

ENTRYPOINT [ "python", "app.py"]