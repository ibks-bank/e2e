import pytest
from framework.logger import Logger
from api_bank_account.service_data.read_json import ReadJson

config = ReadJson()
config.read_json()


@pytest.fixture()
def clear_logger():
    Logger.clear_logger()
