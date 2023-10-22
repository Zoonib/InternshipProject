from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By


class PageOpens(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='menu-button-text']")
    def click_left_side_menu(self):
        self.driver.get('https://soft.reelly.io/')

        sleep(2)
        self.driver.refresh()

    def verify_right_page_opens(self):
        self.driver.get('https://soft.reelly.io/')