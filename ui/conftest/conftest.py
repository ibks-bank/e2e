import pytest
from framework.logger import Logger
from ui.service_data.read_json import ReadJson

config = ReadJson()


@pytest.fixture()
def clear_logger():
    Logger.clear_logger()
