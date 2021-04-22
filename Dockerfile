FROM python:alpine

WORKDIR /discord-bot

RUN apk update && apk add python3-dev gcc libc-dev
RUN pip3 install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "./main.py"]