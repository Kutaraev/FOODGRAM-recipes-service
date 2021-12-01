FROM python:3.7

RUN mkdir /code
COPY . /code

RUN pip install -r /code/requirements.txt

CMD python3 manage.py makemigrations &&\
 python3 manage.py migrate &&\
 gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000

WORKDIR /code
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
