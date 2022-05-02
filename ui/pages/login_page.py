from framework.string import String
from framework.input_field import Filed
from framework.button import Button


class LoginPage:
    def __init__(self):
        self.welcome_str = String("//h2[@class='text-center']")
        self.name = Filed("//input[@class='form-control']")
        self.password = Filed("//input[@class='password-field']")
        self.log_in = Button("//div//button[@class]")
        self.code = Filed("//input[@name='code']")
        self.code_text = String("//label[@for='code']")
        self.register = Button("//a[@href='/register']")

    def check_login_page(self):
        return self.welcome_str.get_text() == "Login To Profile"

    def check_reg_str(self):
        return self.register.find_element_by_xpath().text == "Are you not registered? Register now"

    def check_code_field(self):
        return self.code_text.get_text() == "Code"

    def fill_fields(self, username, password):
        self.name.input_data(username)
        self.password.input_data(password)

    def enter_code(self, data):
        self.code.input_data(data)

    def click_registration(self):
        self.register.set_element(self.register.find_element_by_xpath())
        self.register.wait_element()
        self.register.click_without_wait()

    def click_login(self):
        self.log_in.set_element(self.log_in.find_element_by_xpath())
        self.log_in.wait_element()
        self.log_in.click_without_wait()
