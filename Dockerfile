FROM python:3.8-slim
# Get envsubst from gettext-base
RUN apt-get update &&\
    apt install gettext-base
RUN pip install requests
WORKDIR /mastodon
COPY . .
CMD envsubst < config.json.example > config.json && python toot.py