FROM python:3.7.4
ENV PYTHONUNBUFFERED 1

# change working directory
RUN mkdir /backend
WORKDIR /backend

# run and upgrade pip
COPY requirements.txt /backend/
RUN pip install pip -U

# install dependencies
RUN pip install -r requirements.txt
COPY . /backend/
