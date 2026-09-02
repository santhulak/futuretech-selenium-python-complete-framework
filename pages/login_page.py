from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.ID, "error-message")
    SUCCESS_MESSAGE = (By.ID, "success-message")
    FORGOT_PASSWORD = (By.ID, "forgot-password")

    def enter_username(self, username):
        self.type_text(self.USERNAME, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_password_type(self):
        return self.get_attribute(self.PASSWORD, "type")

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)
