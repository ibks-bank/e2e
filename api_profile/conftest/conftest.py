import pytest
from framework.logger import Logger
from api_profile.service_data.read_json import ReadJson

config = ReadJson()


@pytest.fixture()
def clear_logger():
    Logger.clear_logger()
