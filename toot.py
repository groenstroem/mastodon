import json
import logging

import requests

logging.basicConfig(level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)

# Get the message to be tooted from the grønstrøm API
overview = requests.get('https://grønstrøm.nu/api/v1/next-day').json()
status = f'{overview["title"]}\n{overview["message"]}'


host_instance = 'https://' + config['mastodon_instance']
token = config['access_token']

headers = {'Authorization': 'Bearer ' + token}

data = {'status': status, 'visibility': 'public'}

response = requests.post(
    url=host_instance + '/api/v1/statuses', data=data, headers=headers)

logging.info(f'Received response {response.status_code}: {response.text}')