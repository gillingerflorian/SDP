# syntax=docker/dockerfile:1

FROM arm32v6/python:3.8-slim-buster

# BASE

WORKDIR /SDP

ENV FLASK_APP=app
EXPOSE 500
COPY requiremnts/base.txt base.txt

RUN pip3 install -r base.txt

COPY . .

CMD [ "FLASK_APP=app" ]
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]


# DEVELOPMENT

WORKDIR /SDP

ENV FLASK_APP=app
ENV FLASK_ENV=development
EXPOSE 500

COPY requiremnts/dev.txt dev.txt

RUN pip3 install -r dev.txt

COPY . .

CMD [ "FLASK_APP=app" ]
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]


# TEST






# PRODUCTION

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]