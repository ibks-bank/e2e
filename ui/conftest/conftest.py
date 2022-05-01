import pytest
from framework.logger import Logger
from framework.browser_factory import BrowserFactory
from ui.service_data.read_json import ReadJson
from ui.pages.login_page import LoginPage

config = ReadJson()
config.read_json()


@pytest.fixture()
def clear_logger():
    Logger.clear_logger()


@pytest.fixture()
def resource_setup(request):
    factory = BrowserFactory()
    browser = factory.init_browser(config.browser[int(config.name_browser)])
    browser.get_page(config.url)
    login_page = LoginPage()

    def resource_teardown():
        browser.close()

    request.addfinalizer(resource_teardown)
    return login_page
