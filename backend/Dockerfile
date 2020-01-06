FROM python:3.7.4
ENV PYTHONUNBUFFERED 1

# change working directory
COPY . /backend/
WORKDIR /backend

# run and upgrade pip
RUN pip install pip -U
ADD requirements.txt /backend/

# install dependencies
RUN pip install -r requirements.txt
ADD . /backend/

# Make port 8000 available for the app
EXPOSE 8000

# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
CMD python3 manage.py runserver 0.0.0.0:8000