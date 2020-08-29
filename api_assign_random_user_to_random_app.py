import requests
import json
import random
import sys

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

params = (
    ('limit', '200'),
)

users = requests.get('https://{}/api/v1/users'.format(okta_domain), headers=headers, params=params)
rand_int = random.randint(0, len(users.json())-1)
# print(json.dumps(response.json()[rand_int], indent=1))
# print(len(json.dumps(response.json())))

rand_user_id = users.json()[rand_int]['id']

rand_user = requests.get('https://{}/api/v1/users/{}'.format(okta_domain, rand_user_id), headers=headers, params=params).json()

apps = requests.get('https://{}/api/v1/apps/'.format(okta_domain), headers=headers)
rand_int = random.randint(0, len(apps.json())-1)

rand_app = apps.json()[rand_int]
rand_app_id = rand_app['id']

# response = requests.get('https://{}/api/v1/apps/{}'.format(okta_domain, rand_app_id), headers=headers)
# print(json.dumps(response.json(), indent=1))

# data = '{ "id": "00u596ox5mq0QPsHM357", "scope": "USER", "credentials": { "userName": "isaac.brock@example.com", "password": { "value": "tlpWENT2m" } } }'

print(rand_user['id'])
print(rand_user['profile']['email'])

rand_user_id = str(rand_user['id'])
rand_user_email = str(rand_user['profile']['email'])
rand_user_pass = str(rand_user['credentials']['password'])

data = '{ "id": "'+rand_user_id+'", "scope": "USER", "credentials": { "userName": "'+rand_user_email+'", "password": '+rand_user_pass+' } }'

response = requests.post('https://{}/api/v1/apps/{}/users'.format(okta_domain, rand_app_id), headers=headers, data=data)

print(rand_app)
print(json.dumps(response.json(), indent=1))

