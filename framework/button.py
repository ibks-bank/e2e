from framework.base_element import BaseElement
from selenium.webdriver.common.action_chains import ActionChains


class Button(BaseElement):
    def move_on_button(self):
        ActionChains(self.driver.get_driver()).move_to_element(self.find_element_by_xpath()).perform()
