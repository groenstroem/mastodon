# Grøn strøm Mastodon bot

This repository contains the code for the Mastodon bot posting automatic updates on the Danish emission intensities,
currently live as [@co2prognoser@mastodon.social](https://mastodon.social/@co2prognoser).


## Configuration

To use this, create a user on a Mastodon instance (e.g. `mastodon.social`), and create an app with that user with rights
to create Mastodon statuses. Note the access token from the Mastodon app.

## Running

With these at hand, fill out `config.json.example` and move the result to `config.json`.

Then to create a Mastodon update with the current emission intensities, get all dependencies and run the only
available script,

```
pip install requests
python toot.py
``` 

## Docker

Alternatively, use Docker, specifying all configuration parameters as environment variables,

```
docker build -t groenstroem-mastodon
docker run -e MASTODON_INSTANCE=mastodon.social -e ACCESS_TOKEN=... groenstroem-mastodon 
``` 