FROM python:3.8.1

ADD . /discord-bot
WORKDIR /discord-bot
ENV TOKEN="NjIzNTIxODM0NzEyODI1ODY2.XeZK2Q.AeeaviRy9sCIPC-XdsZ_KmixJBQ" APIKEY="AIzaSyAdQH2zJq1EfgW82ktUS7VgMM-v_tb37as"

RUN ls
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]