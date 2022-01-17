FROM ubuntu:20.04
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip3 install -r requirements.txt
#RUN rm requirements.txt
WORKDIR /
VOLUME /src


EXPOSE 8000
