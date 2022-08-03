FROM python:3.9 as django-build

RUN apt-get update && apt-get install -y gettext

COPY requirements.txt /app/requirements.txt
RUN pip install --no-deps --no-cache-dir -r /app/requirements.txt

WORKDIR /app/
COPY . /app/

RUN python manage.py compilemessages


ENV PORT=80
CMD uwsgi --http=0.0.0.0:$PORT --module=backend.wsgi --master --workers=4 --max-requests=1000 --lazy-apps --need-app --http-keepalive --harakiri 65 --vacuum --strict --single-interpreter --die-on-term --disable-logging --log-4xx --log-5xx --cheaper=2 --enable-threads