FROM python:2.7.12-slim
MAINTAINER Karakulov I <Ikarakulov@techinfocom.com>
RUN mkdir /service
WORKDIR /service 
ADD serv.py /service
EXPOSE 8881
CMD [ "python", "./serv.py" ]
