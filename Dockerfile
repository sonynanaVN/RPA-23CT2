FROM python:3.13
WORKDIR /usr/local/app

COPY mail ./mail

RUN useradd -m app
USER app

CMD ["python", "mail/automail.py"]
#docker run
docker run automail:latest