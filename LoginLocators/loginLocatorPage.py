# pages/locator_page.py

from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Class to store locators for the login page."""
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3')
