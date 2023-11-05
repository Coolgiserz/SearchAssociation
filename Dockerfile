FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/code/search_association
WORKDIR /root/code/search_association

RUN pip install pip -U

ADD requirements.txt /root/code/

RUN pip install -r ../requirements.txt
EXPOSE 8000
ADD ./search_association /root/code