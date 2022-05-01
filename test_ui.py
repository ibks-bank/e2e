from ui.conftest.conftest import clear_logger
from ui.conftest.conftest import resource_setup
from ui.service_data.read_json import ReadJson

config = ReadJson()
config.read_json()


def test_check_login_page(resource_setup, clear_logger):
    home_page = resource_setup

