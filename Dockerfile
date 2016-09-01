FROM debian:jessie

RUN apt-get update 

RUN apt-get install -y curl
COPY treetagger_builder/builder/scripts/make.bash treetagger_builder/builder/scripts/install.bash /
RUN /make.bash -r 3.2; 
RUN rm -rf /var/tmp/*; 
RUN mv treetagger.tar.gz /usr/local; 
RUN cd /usr/local; tar -xzf treetagger.tar.gz; rm treetagger.tar.gz; 
RUN cd /usr/local/lib; rm bulgarian* dutch* esto* fin* gal* latin* mongo* pol* romani* russi* slova* swahi*
WORKDIR /
RUN chmod +x /usr/local/cmd/*
ENV PATH $PATH:/usr/local/cmd

RUN apt-get install -y python python-dev python-distribute python-pip perl
RUN pip install nltk numpy

WORKDIR /root

RUN mkdir /time_extract
WORKDIR /time_extract

ADD ./requirements.txt /time_extract/requirements.txt
ADD ./requirements.test.txt /time_extract/requirements.test.txt

RUN pip install -r requirements.txt
RUN pip install -r requirements.test.txt

EXPOSE 8080
