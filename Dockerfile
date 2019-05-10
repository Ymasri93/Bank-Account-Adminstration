FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /bank-account-administration
WORKDIR /bank-account-administration
ADD requirements.txt /bank-account-administration/
RUN pip install -r requirements.txt
ADD . /bank-account-administration
