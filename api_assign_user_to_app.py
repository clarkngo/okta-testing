import requests
import json

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

data = '{ "id": "00u596ox5mq0QPsHM357", "scope": "USER", "credentials": { "userName": "isaac.brock@example.com", "password": { "value": "tlpWENT2m" } } }'

app_id = '0oa41qm1wvQ8r6Vvm357'

response = requests.post('https://{}/api/v1/apps/{}/users'.format(okta_domain, app_id), headers=headers, data=data)

print(json.dumps(response.json(), indent=1))
