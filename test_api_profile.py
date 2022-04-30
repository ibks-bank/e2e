import ast

from api_profile.conftest.conftest import clear_logger
from api_profile.conftest.conftest import get_wrong_login_and_password
from api_bank_account.conftest.conftest import registration
from api_profile.service_data.read_json import ReadJson
from framework.logger import Logger

import requests
import json
import random

config = ReadJson()
config.read_json()

base_url = "http://{ip}:{port}/".format(ip=str(config.ip), port=str(config.port))


def test_successful_registration(clear_logger):
    Logger.logging_info_data("Test 1. Check API successful registration")
    path = "v1/auth/sign-up"
    data = {
        "email": "test" + config.mail,
        "password": "test" + config.password,
        "passport": {
            "series": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(4)]),
            "number": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(6)]),
            "firstName": config.first_name,
            "middleName": config.second_name,
            "lastName": config.second_name,
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
    assert response.status_code == 200, Logger.logging_info_data("Test 1. FAILED")
    Logger.logging_info_data("Test 1. PASS")


def test_unsuccessful_registration():
    Logger.logging_info_data("Test 2. Check API unsuccessful registration")
    path = "v1/auth/sign-up"
    data = {
        "email": config.mail,
        "password": config.password,
        "passport": {
            "series": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(4)]),
            "number": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(6)]),
            "firstName": config.first_name,
            "middleName": config.second_name,
            "lastName": config.second_name,
            "issuedBy": "RUSSIA",
            "issuedAt": "2000-01-01T16:53:20.724Z",
            "address": "St.Petersburg",
            "birthplace": "St.Petersburg",
            "birthdate": "1990-01-01"
        }
    }

    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    response_json = json.loads(response.text)
    assert response.status_code == 400, Logger.logging_info_data("Test 2. FAILED")
    Logger.logging_info_data("Test 2. PASS")


def test_successful_sign_in_without_code():
    Logger.logging_info_data("Test 3. Check API successful sign in")
    path = "v1/auth/sign-in"
    data = {
        "email": "test" + config.mail,
        "password": "test" + config.password,
    }

    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    response_json = json.loads(response.text)
    assert response.status_code == 200, Logger.logging_info_data("Test 3. FAILED")
    Logger.logging_info_data("Test 3. PASS")


def test_unsuccessful_sign_in(get_wrong_login_and_password):
    login, password = get_wrong_login_and_password
    Logger.logging_info_data("Test 4. Check API unsuccessful sign in with login {} and password {}".format(login,
                                                                                                           password))
    path = "v1/auth/sign-in"
    data = {
        "email": login,
        "password": password,
    }

    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    response_json = json.loads(response.text)
    assert response.status_code == 404, Logger.logging_info_data("Test 4. FAILED with login {} and password {}"
                                                                 .format(login, password))
    Logger.logging_info_data("Test 4. PASS with login {} and password {}".format(login, password))


def test_full_successful_sign_in():
    Logger.logging_info_data("Test 5. Check API full sign in")
    Logger.logging_info_data("Sign up new user")
    path = "v1/auth/sign-up"
    data = {
        "email": config.mail,
        "password": config.password,
        "passport": {
            "series": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(4)]),
            "number": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(6)]),
            "firstName": config.first_name,
            "middleName": config.second_name,
            "lastName": config.second_name,
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
        "email": config.mail,
        "password": config.password,
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
        "email": config.mail,
        "password": config.password,
        "code": "1234"
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    assert response.status_code == 200, Logger.logging_info_data("Test 5. FAILED with sending code to backend")
    Logger.logging_info_data("Test 5. PASS")


def test_get_passport(registration):
    Logger.logging_info_data("Test 6. Check API get passport")
    path = "v1/passport"
    response = registration
    token = response.content
    token = ast.literal_eval(token.decode('utf-8'))
    headers = {
        'X-Auth-Token': str(token['token'])
    }
    request = requests.get(url=base_url + path, headers=headers)
    assert request.status_code == 200, Logger.logging_info_data("Test 6. FAILED")
    Logger.logging_info_data("Test 6. PASS")
