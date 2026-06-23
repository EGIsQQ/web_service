FROM python:3.14-slim

WORKDIR /code 

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY  . . 

ENV FLASK_APP=app.py 


CMD flask run -h 0.0.0.0 -p 80
