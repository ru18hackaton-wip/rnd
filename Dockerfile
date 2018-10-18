FROM ev3dev/ev3dev-stretch-ev3-generic
RUN apt-get update && apt-get -qq -y install python3-pip
ADD requirements.txt /app/
WORKDIR /app
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

ENV PYTHONIOENCODING=utf8

CMD ["python3", "app.py"]
