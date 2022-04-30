import json
import random
import string
import pytest
import requests

from framework.logger import Logger
from api_profile.service_data.read_json import ReadJson

config = ReadJson()
config.read_json()

base_url = "http://{ip}:{port}/".format(ip=str(config.ip), port=str(config.port))


@pytest.fixture()
def clear_logger():
    Logger.clear_logger()


@pytest.fixture()
def registration():
    path = "v1/auth/sign-up"
    email = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(3)]) + '@' + \
            ''.join([random.choice(string.ascii_letters + string.digits) for n in range(3)]) + ".com"
    data = {
        "email": email,
        "password": "ibksizi!",
        "passport": {
            "series": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(4)]),
            "number": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(6)]),
            "firstName": "QA",
            "middleName": "QA",
            "lastName": "QA",
            "issuedBy": "RUSSIA",
            "issuedAt": "2000-01-01T16:53:20.724Z",
            "address": "St.Petersburg",
            "birthplace": "St.Petersburg",
            "birthdate": "1990-01-01T16:53:20.724Z"
        }
    }

    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    response_json = json.loads(response.text)
    assert response.status_code == 200, Logger.logging_info_data("Test 5. FAILED on sign up")
    user_id = response_json["userID"]

    Logger.logging_info_data("Sign in with new user")
    path = "v1/auth/sign-in"
    data = {
        "email": email,
        "password": "ibksizi!",
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    response_json = json.loads(response.text)
    assert response.status_code == 200, Logger.logging_info_data("Test 5. FAILED with sign in")

    Logger.logging_info_data("Getting code")
    path = "v1/qa-api/set-code"
    data = {
        "code": "1234",
        "userID": str(user_id)
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    assert response.status_code == 200, Logger.logging_info_data("Test 5. FAILED with internal QA api")

    Logger.logging_info_data("Enter user code")
    path = "v1/auth/submit-code"
    data = {
        "email": email,
        "password": "ibksizi!",
        "code": "1234"
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    return response
