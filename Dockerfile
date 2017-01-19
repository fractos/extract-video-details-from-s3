FROM ubuntu
MAINTAINER Adam Christie <adam.christie@digirati.co.uk>

RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential ffmpeg
COPY app /opt/extract-details
RUN pip install -r /opt/extract-details/requirements.txt
WORKDIR /opt/extract-details
