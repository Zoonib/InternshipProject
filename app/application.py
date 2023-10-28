from pages.main_page import MainPage
from pages.log_in_page import LogInPage
from pages.page_opens import PageOpens
from pages.filter_products import FilterResultPage



class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.log_in_page= LogInPage(driver)
        self.page_opens = PageOpens(driver)
        self.filter_products = FilterResultPage(driver)
