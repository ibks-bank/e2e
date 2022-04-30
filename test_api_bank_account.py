import ast

from api_bank_account.conftest.conftest import clear_logger
from api_bank_account.conftest.conftest import registration
from api_bank_account.service_data.read_json import ReadJson
from framework.logger import Logger

import requests
import json
import random

config = ReadJson()
config.read_json()

base_url = "http://{ip}:{port}/".format(ip=str(config.ip), port=str(config.port))


def test_get_accounts(clear_logger, registration):
    Logger.logging_info_data("Test 1. Check API get accounts")
    path = "v1/accounts"
    response = registration
    token = response.content
    token = ast.literal_eval(token.decode('utf-8'))
    headers = {
        'X-Auth-Token': str(token['token'])
    }
    request = requests.get(url=base_url + path, headers=headers)
    assert request.status_code == 200, Logger.logging_info_data("Test 1. FAILED with getting accounts")
    Logger.logging_info_data("Test 1. PASS")


def test_successful_create_account(registration):
    Logger.logging_info_data("Test 2. Check API create account")
    path = "v1/accounts/create"
    response = registration
    token = response.content
    token = ast.literal_eval(token.decode('utf-8'))
    headers = {
        'X-Auth-Token': str(token['token'])
    }
    data = {
        "currency": "CURRENCY_RUB",
        "limit": "10000",
        "name": "test"
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, headers=headers, json=json.loads(json_data))
    assert response.status_code == 200, Logger.logging_info_data("Test 2. FAILED with creating new account")
    Logger.logging_info_data("Test 2. PASS")


def test_unsuccessful_create_account(registration):
    Logger.logging_info_data("Test 3. Check API unsuccessful create account")
    path = "v1/accounts/create"
    response = registration
    token = response.content
    token = ast.literal_eval(token.decode('utf-8'))
    headers = {
        'X-Auth-Token': str(token['token'])
    }
    data = {
        "currency": "CURRENCY_RUB",
        "limit": "-10000",
        "name": "test"
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, headers=headers, json=json.loads(json_data))
    assert response.status_code == 400, Logger.logging_info_data("Test 2. FAILED with unsuccessful creating new account")
    Logger.logging_info_data("Test 2. PASS")


def test_get_certain_account(registration):
    path = "v1/accounts/create"
    response = registration
    token = response.content
    token = ast.literal_eval(token.decode('utf-8'))
    headers = {
        'X-Auth-Token': str(token['token'])
    }
    data = {
        "currency": "CURRENCY_RUB",
        "limit": "10000",
        "name": "test"
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, headers=headers, json=json.loads(json_data))
    account_id = response.content
    account_id = ast.literal_eval(account_id.decode('utf-8'))
    Logger.logging_info_data("Test 4. Check API get certain account")
    path = "v1/accounts/" + str(account_id['accountID'])

    response = registration
    token = response.content
    token = ast.literal_eval(token.decode('utf-8'))
    headers = {
        'X-Auth-Token': str(token['token'])
    }
    request = requests.get(url=base_url + path, headers=headers)
    assert request.status_code == 200, Logger.logging_info_data("Test 4. FAILED with getting certain account")
    Logger.logging_info_data("Test 4. PASS")
    return str(account_id['accountID']), str(token['token'])


def test_fill_account(registration):
    Logger.logging_info_data("Test 5. Check API fill balance")
    id, token = test_get_certain_account(registration)
    path = "v1/accounts/" + str(id) + "/fill-balance"
    headers = {
        'X-Auth-Token': token
    }
    data = {
        "accountID": str(id),
        "amount": "10000"
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, headers=headers, json=json.loads(json_data))
    assert response.status_code == 200, Logger.logging_info_data("Test 5. FAILED with filling the balance")
    Logger.logging_info_data("Test 5. PASS")


def test_get_transactions(registration):
    Logger.logging_info_data("Test 6. Check API transactions")
    path = "v1/transactions"
    response = registration
    token = response.content
    token = ast.literal_eval(token.decode('utf-8'))
    headers = {
        'X-Auth-Token': str(token['token'])
    }
    request = requests.get(url=base_url + path, headers=headers)
    assert request.status_code == 200, Logger.logging_info_data("Test 6. FAILED with transactions")
    Logger.logging_info_data("Test 6. PASS")


def test_unsuccessful_create_transactions(registration):
    Logger.logging_info_data("Test 7. Check API unsuccessful create transaction")
    id, token = test_get_certain_account(registration)
    path = "v1/transactions/create"
    headers = {
        'X-Auth-Token': token
    }
    data = {
        "accountID": str(id),
        "payee": str(id),
        "amount": "10"
    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url=base_url + path, headers=headers, json=json.loads(json_data))
    assert response.status_code == 400, Logger.logging_info_data("Test 7. FAILED with unsuccessful creating the transaction")
    Logger.logging_info_data("Test 7. PASS")
