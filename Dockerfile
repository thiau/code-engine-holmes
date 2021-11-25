FROM python:3.8

RUN mkdir app

COPY app.py app/app.py
COPY server app/server
COPY requirements.txt app/requirements.txt

RUN pip3 install -r app/requirements.txt

EXPOSE 7000

WORKDIR app
ENTRYPOINT ["python3", "app.py"]