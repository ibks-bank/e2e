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


