FROM python:3.13-alpine

WORKDIR /app

RUN pip install pyzmq

COPY cliente.py .
COPY broker.py .

CMD ["python", "cliente.py"]