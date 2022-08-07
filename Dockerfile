FROM python:3.9 as django-build

RUN apt-get update && apt-get install -y gettext

COPY requirements.txt /app/requirements.txt
RUN pip install --no-deps --no-cache-dir -r /app/requirements.txt

WORKDIR /app/
COPY . /app/

RUN python manage.py compilemessages

RUN python manage.py collectstatic --noinput

EXPOSE 80

ENV PORT=80
CMD uwsgi --module=articles.wsgi --http=0.0.0.0:$PORT