from selenium.webdriver.common.by import By
from pages.base_page import Page

class LogInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='sign-in-text']")
    def verify_LogIn_opened(self, expected_result):
        self.verify_LogIn_opened(expected_result, *self.SIGNIN_HEADER)