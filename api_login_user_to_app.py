import requests
import sys
import json
import time
import random
import string



import requests
import json
import random

def load_json_file(json_filename):
    with open(json_filename) as json_file:
        json_data = json.load(json_file)
        return json_data

def authenticate_user(username, password):
    app_endpoint = "https://{}/api/v1/authn".format(okta_domain)
    data = {
        "username": username,
        "password": password,
        "options": {
            "multiOptionalFactorEnroll": False,
            "warnBeforePasswordExpired": False
        }
    }
    r = requests.post(url=app_endpoint, json=data, headers=headers)

    if r.status_code != 200:
        sys.stderr.write("Failed to authenticate user {}: {}\n{}\n".format(username,
                                                                           r.status_code, r.json()))
        return None

    return r.json()

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

rand_user_from_an_app = requests.get('https://{}/api/v1/users/{}'.format(okta_domain,rand_user_id), headers=headers, params=params).json()


print(json.dumps(rand_user_from_an_app, indent=1))


# print(rand_user_from_an_app["profile"])
print("User email: {}".format(rand_user_from_an_app["profile"]["email"]))
# authenticate_user(rand_user_from_an_app["profile"]["email"], rand_user_from_an_app["credentials"]["password"]")
auth_user = authenticate_user("cetesting10+genr@gmail.com", "test123")

print(json.dumps(auth_user, indent=1))
