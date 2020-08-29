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

app_id='0oa43a1vo3Xwq2S6X357'

response = requests.get('https://{}/api/v1/apps/{}'.format(okta_domain, app_id), headers=headers)
print(json.dumps(response.json(), indent=1))
