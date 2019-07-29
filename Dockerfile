FROM python:3.7

ADD ./src /src
RUN pip3 install git+https://github.com/channelcat/sanic
# RUN pip3 install git+https://github.com/prometheus/client_python

EXPOSE 8000

WORKDIR /src

CMD ["python", "main.py"]