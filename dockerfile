FROM python:3.8-slim-buster
RUN mkdir /tcp_server
WORKDIR /tcp_server
ADD . /tcp_server
CMD ["python3", "tcp_server.py"]

