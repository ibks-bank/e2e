class Browser:
    instance = None

    @staticmethod
    def inst(driver):
        if Browser.instance is None:
            Browser.instance = Browser(driver)
        return Browser.instance

    def __init__(self, driver):
        self.driver = driver

    def get_page(self, name):
        return self.driver.get(name)

    def change_window(self, window):
        self.driver.switch_to_window(self.driver.window_handles[window])

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.close()
        Browser.instance = None