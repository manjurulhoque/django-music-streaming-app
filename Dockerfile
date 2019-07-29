FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/html/djangomusicapp
WORKDIR /var/www/html/djangomusicapp
COPY requirements.txt /var/www/html/djangomusicapp
RUN pip install -r requirements.txt
COPY . /var/www/html/djangomusicapp
