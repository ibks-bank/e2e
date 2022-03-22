from api_profile.conftest.conftest import clear_logger
from api_profile.service_data.read_json import ReadJson
from framework.logger import Logger

import requests
import json
import random

necessary_information = ReadJson()
necessary_information.read_json()

base_url = "http://{ip}:{port}/".format(ip=str(necessary_information.ip), port=str(necessary_information.port))


def test_successful_registration(clear_logger):
    Logger.logging_info_data("Test 1. Check API successful registration")
    path = "v1/auth/sign-up"
    data = {
        "email": necessary_information.mail,
        "password": necessary_information.password,
        "passport": {
            "series": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(4)]),
            "number": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(6)]),
            "firstName": necessary_information.first_name,
            "middleName": necessary_information.second_name,
            "lastName": necessary_information.second_name,
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
        "email": necessary_information.mail,
        "password": necessary_information.password,
        "passport": {
            "series": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(4)]),
            "number": ''.join(str(item) for item in [random.randint(0, 9) for _ in range(6)]),
            "firstName": necessary_information.first_name,
            "middleName": necessary_information.second_name,
            "lastName": necessary_information.second_name,
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


def test_successful_sign_in():
    Logger.logging_info_data("Test 3. Check API successful sign in")
    path = "v1/auth/sign-in"
    data = {
        "email": necessary_information.mail,
        "password": necessary_information.password,
    }

    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    response_json = json.loads(response.text)
    assert response.status_code == 200, Logger.logging_info_data("Test 3. FAILED")
    Logger.logging_info_data("Test 3. PASS")


def test_successful_sign_in():
    Logger.logging_info_data("Test 4. Check API unsuccessful sign in")
    path = "v1/auth/sign-in"
    data = {
        "email": necessary_information.mail,
        "password": necessary_information.password,
    }

    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, json=json.loads(json_data))
    response_json = json.loads(response.text)
    assert response.status_code == 200, Logger.logging_info_data("Test 4. FAILED")
    Logger.logging_info_data("Test 4. PASS")
    