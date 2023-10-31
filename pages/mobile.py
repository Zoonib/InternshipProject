from selenium.webdriver.common.by import By
from pages.base_page import Page


class MobilePage(Page):
    FILTER_BTN = (By.CSS_SELECTOR, 'div[wized="openFiltersWindow"]')
    #FILTER_FIRST = (By.CSS_SELECTOR, '.input-lield-text.w-input#field-5')
    FILTER_FIRST = (By.CSS_SELECTOR, 'input.input-lield-text[wized="unitPriceFromFilter"]')
    First = ('1200000')
    #FILTER_SEC = (By.CSS_SELECTOR, '.input-lield-text.w-input#field-5')
    FILTER_SEC = (By.CSS_SELECTOR, 'input.input-lield-text[wized="unitPriceToFilter"]')
    Sec = ('2000000')

    def filter_btn(self):
        self.click(*self.FILTER_BTN)

    def filter_first(self):
        self.input_text(self.First, *self.FILTER_FIRST)


