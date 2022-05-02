import time

from ui.conftest.conftest import clear_logger
from ui.conftest.conftest import resource_setup
from ui.service_data.read_json import ReadJson
from framework.logger import Logger

config = ReadJson()
config.read_json()


def test_check_login_page(resource_setup, clear_logger):
    home_page = resource_setup
    Logger.logging_info_data("Test 1. Go to the site")
    Logger.logging_info_data("Check that this is our bank")
    assert home_page.check_login_page() is True, Logger.logging_info_data("Test 1. FAILED")
    Logger.logging_info_data("Test 1. PASS")


def test_enter_credentials(resource_setup):
    home_page = resource_setup
    Logger.logging_info_data("Test 2. Go to the site")
    username = config.username
    password = config.password
    Logger.logging_info_data("Test 2. Enter username and password")
    home_page.fill_fields(username, password)
    Logger.logging_info_data("Test 2. Click login")
    home_page.login()
    Logger.logging_info_data("Test 2. Check field appears")
    assert home_page.check_code_field() is True, Logger.logging_info_data("Test 2. FAILED")
    Logger.logging_info_data("Test 2. PASS")

