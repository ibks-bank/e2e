import pytest
from framework.logger import Logger
from api_profile.service_data.read_json import ReadJson

config = ReadJson()
config.read_json()


@pytest.fixture()
def clear_logger():
    Logger.clear_logger()


@pytest.fixture(params=[(config.mail + "q", config.password), (config.mail, config.password + "q"), (config.mail + "q",
                        config.password + "q")])
def get_wrong_login_and_password(request):
    return request.param
