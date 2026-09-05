FROM python:3.13-alpine

WORKDIR /app

RUN pip install pyzmq

COPY servidor.py .

CMD ["python", "servidor.py"]