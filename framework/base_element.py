from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.browser_factory import BrowserFactory
from ui.service_data.read_json import ReadJson

config = ReadJson()
config.read_json()


class BaseElement:
    def __init__(self, locator):
        self.driver = BrowserFactory().init_browser("Chrome")
        self.locator = locator
        self.wait = WebDriverWait(self.driver.get_driver(), config.wait_time)
        self.element = None

    def find_elements_by_xpath(self):
        return self.driver.get_driver().find_elements_by_xpath(self.locator)

    def send_key(self):
        return self.driver.get_driver()

    def find_element_by_xpath(self):
        return self.driver.get_driver().find_element_by_xpath(self.locator)

    def find_element_by_css(self):
        return self.driver.get_driver().find_element_by_css_selector(self.locator)

    def find_elements_by_css(self):
        return self.driver.get_driver().find_elements_by_css_selector(self.locator)

    def find_element_by_id(self):
        return self.driver.get_driver().find_element_by_id(self.locator)

    def wait_element(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.locator)))

    def wait_element_vision(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator)))

    def wait_implicitly(self):
        self.driver.get_driver().implicitly_wait(config.wait_time)

    def get_element(self):
        return self.element

    def set_element(self, obj):
        self.element = obj

    def click_without_wait(self):
        element = self.get_element()
        element.click()