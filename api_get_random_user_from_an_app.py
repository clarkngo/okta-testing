import requests
import json
import random

def load_json_file(json_filename):
    with open(json_filename) as json_file:
        json_data = json.load(json_file)
        return json_data

cfg_somecorp = load_json_file("config_somecorp.json")
okta_domain = cfg_somecorp["okta_domain"]
api_key = cfg_somecorp["api_key"]


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'SSWS {}'.format(api_key),
}

# testingtime
app_id='0oa43a1vo3Xwq2S6X357'

response = requests.get('https://{}/api/v1/apps/{}/users'.format(okta_domain, app_id), headers=headers)

params = (
    ('limit', '200'),
)

rand_int = random.randint(0, len(response.json())-1)

rand_user_id = response.json()[rand_int]['id']

response = requests.get('https://{}/api/v1/users/{}'.format(okta_domain,rand_user_id), headers=headers, params=params)
print(json.dumps(response.json(), indent=1))
