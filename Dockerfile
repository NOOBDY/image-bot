FROM python:3.8.1

ADD . /discord-bot
WORKDIR /discord-bot

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]