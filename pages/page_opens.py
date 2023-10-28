from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageOpens(Page):

    SIGNIN_HEADER = (By.XPATH, "//h1[@class='menu-button-text']")
    secondary_page = (By.CSS_SELECTOR, 'div.div-block-33 div.menu-button-text')
    verify_page = (By.XPATH, "//div[@class= 'menu-button-text'(Secondary)]")
    def click_left_side_menu(self):
        # self.driver.get('https://soft.reelly.io/secondary-listings/')
        # self.wait_for_element_clickable(*self.secondary_page)
        self.click(*self.secondary_page)

        sleep(2)

    def verify_right_page_open(self):
        self.verify_partial_url('secondary-listings')
        #self.driver.refresh()
        sleep(3)