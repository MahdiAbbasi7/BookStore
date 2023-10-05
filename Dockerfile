FROM ubuntu:latest
LABEL authors="mahdi"

ENTRYPOINT ["top", "-b"]

# Pull base image
FROM python:3.10
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work dir
WORKDIR /book
# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
# Copy project
COPY . /book/
