FROM python:3

ADD . /app

WORKDIR /app

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

CMD ["python", "api.py"]

EXPOSE 8888