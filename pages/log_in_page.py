from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class LogInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='sign-in-text']")
    Email = (By.CSS_SELECTOR, '.input#email-2')
    Password = (By.CSS_SELECTOR, '.input#field')
    Continue = (By.CSS_SELECTOR, '.login-button.w-button')
    Email_Input = 'zooni.b8@gmail.com'
    Password_Input = 'Tester.2000'


    def email_log_in(self):
        self.input_text(self.Email_Input, *self.Email)
        sleep(2)

    def password_log_in(self):
        self.input_text(self.Password_Input, *self.Password)
        sleep(2)

    def continue_button(self):
        self.click(*self.Continue)


