# pages/action_page.py
from LoginLocators.loginLocatorPage import LoginPageLocators


class LoginPageActions:
    """Class to perform actions on the login page using the locators."""

    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators()

    def enter_username(self, username):
        self.driver.find_element(*self.locators.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.locators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.locators.ERROR_MESSAGE).text
