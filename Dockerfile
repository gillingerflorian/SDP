# syntax=docker/dockerfile:1

FROM arm32v6/python:3.9-alpine as base
RUN apk update
RUN apk add python3-dev \
            gcc \
            libc-dev \
            libffi-dev

# BASE

WORKDIR /SDP

ENV FLASK_APP=app
EXPOSE 500
COPY requirements/base.txt ./requirements/base.txt

RUN pip3 install -r ./requirements/base.txt

COPY . .


CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]


# DEVELOPMENT

FROM base as development
COPY requirements/dev.txt ./requirements/dev.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development
EXPOSE 500

RUN pip3 install -r ./requirements/dev.txt


COPY . .

CMD [ "flask", "--debug", "run", "--host=0.0.0.0"]


# TEST
FROM base as test
COPY requirements/test.txt ./requirements/test.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development
EXPOSE 500

RUN pip3 install -r ./requirements/dev.txt


COPY . .

CMD [ "flask", "--debug", "run", "--host=0.0.0.0"]

# run Unit tests

# run Integration tests



# PRODUCTION

FROM base as production
COPY requirements/dev.txt ./requirements/prod.txt

ENV FLASK_APP=app
EXPOSE 500

RUN pip3 install -r ./requirements/prod.txt


COPY . .

CMD [ "flask", "--debug", "run", "--host=0.0.0.0"]