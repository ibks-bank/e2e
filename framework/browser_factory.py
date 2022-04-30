from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from framework.browser import Browser
from selenium import webdriver


class BrowserFactory:
    def __init__(self):
        self.name = ''

    def init_browser(self, name_of_browser):
        self.name = name_of_browser
        if name_of_browser == "Chrome":
            if Browser.instance is None:
                chrome_options = webdriver.ChromeOptions()
                return Browser.inst(webdriver.Chrome(executable_path=ChromeDriverManager().
                                                     install(), chrome_options=chrome_options))
            else:
                return Browser.instance
        elif name_of_browser == "Firefox":
            if Browser.instance is None:
                parameters = webdriver.FirefoxProfile()
                return Browser.inst(webdriver.Firefox(executable_path=GeckoDriverManager().
                                                      install(), firefox_profile=parameters))
            else:
                return Browser.instance
