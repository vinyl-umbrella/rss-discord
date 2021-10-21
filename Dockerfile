FROM python:3.10-slim-buster
COPY  ./src/ /src

RUN apt-get update && \
    apt-get install -y cron && \
    pip install -r /src/requirements.txt && \
    echo '*/10 * * * * /usr/local/bin/python /src/rss.py' >> /etc/crontab
