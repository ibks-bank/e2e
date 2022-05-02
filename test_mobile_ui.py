from ui.conftest.conftest import clear_logger
from ui.conftest.conftest import resource_setup
from ui.pages.login_page import LoginPage
from appium import webdriver
from framework.logger import Logger


def test_first():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0.0',
        'deviceName': 'emulator-5554',
        'browserName': 'Chrome'
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.get("http://bank.sytes.net:3030/")
    assert driver.find_element_by_xpath("//h2[@class='text-center']").text == "Login To Profile", \
        Logger.logging_info_data("Test 1. FAILED")
    Logger.logging_info_data("Test 1. PASS")
