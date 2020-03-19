FROM python:3.7.7-alpine3.10

RUN pip install requests

ADD . .

ENTRYPOINT [ "python", "tesla.py" ]
