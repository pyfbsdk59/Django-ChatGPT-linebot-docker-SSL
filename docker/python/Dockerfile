FROM python:3.8-buster
	
	
RUN apt-get update

COPY requirements.txt /requirements.txt

RUN apt-get clean

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip freeze > newreqs.txt
COPY uwsgi.ini /uwsgi.ini
CMD ["uwsgi", "--ini", "/uwsgi.ini"]
