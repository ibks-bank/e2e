from framework.input_field import Filed
from framework.button import Button


class RegistrationPage:
    def __init__(self):
        self.__name = "Qa"
        self.email = Filed("//input[@class='form-control']")
        self.password = Filed("//input[@name='password']")
        self.confirm_password = Filed("//input[@name='confPass']")
        self.next = Button("//button[@class='btn btn-primary']")
        self.first_name = Filed("//input[@name='firstName']")
        self.middle_name = Filed("//input[@name='middleName']")
        self.last_name = Filed("//input[@name='lastName']")
        self.birthplace = Filed("//input[@name='birthplace']")
        self.birthdate = Filed("//input[@name='birthdate']")
        self.series = Filed("//input[@name='series']")
        self.number = Filed("//input[@name='number']")
        self.issued = Filed("//input[@name='issuedBy']")
        self.issued_date = Filed("//input[@name='issuedAt']")
        self.address = Filed("//input[@name='address']")

    def registration(self, email, password):
        self.email.input_data(email)
        self.password.input_data(password)
        self.confirm_password.input_data(password)
        self.click_next()
        self.first_name.input_data(self.__name)
        self.middle_name.input_data(self.__name)
        self.last_name.input_data(self.__name)
        self.birthplace.input_data(self.__name)
        self.birthdate.input_data("24.09.2000")

    def continue_registration(self):
        self.series.input_data("1111")
        self.number.input_data("222222")
        self.issued.input_data("MVD")
        self.issued_date.input_data("15.10.2010")
        self.address.input_data("SPB")
        self.click_next()

    def click_next(self):
        self.next.set_element(self.next.find_element_by_xpath())
        self.next.wait_element()
        self.next.click_without_wait()
