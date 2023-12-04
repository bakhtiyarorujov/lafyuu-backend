FROM python:3.8

ARG DIR=/code

WORKDIR $DIR

RUN apt update

COPY requirements.txt ./

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uwsgi", "--ini", "uwsgi.ini"]