FROM python:3.10-alpine

ENV host='0.0.0.0'
ENV port=5000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python3", "main.py" ]
