from framework.string import String


class LoginPage:
    def __init__(self):
        self.welcome_str = String("//h2[@class='text-center']")

    def check_login_page(self):
        return self.welcome_str.get_text() == "Login To Profile"
