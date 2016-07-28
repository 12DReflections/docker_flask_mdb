FROM python:2.7
ADD . /todo
WODIR /todo
RUN pip install -r requirements.txt