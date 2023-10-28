from selenium.webdriver.common.by import By
from pages.base_page import Page


class FilterResultPage(Page):
    FILTER_RESULT = (By.CSS_SELECTOR, '.filter-text')
    #FILTER_FIRST = (By.CSS_SELECTOR, '.input-lield-text.w-input#field-5')
    FILTER_FIRST = (By.CSS_SELECTOR, 'input.input-lield-text[wized="unitPriceFromFilter"]')
    First = ('1200000')
    #FILTER_SEC = (By.CSS_SELECTOR, '.input-lield-text.w-input#field-5')
    FILTER_SEC = (By.CSS_SELECTOR, 'input.input-lield-text[wized="unitPriceToFilter"]')
    Sec = ('2000000')




    def filter_btn(self):
        self.click(*self.FILTER_RESULT)

    def filter_first(self):
        self.input_text(self.First, *self.FILTER_FIRST)

    def filter_second(self):
        self.input_text(self.Sec, *self.FILTER_SEC)

    def verify_info(self):
        actual_name = self.find_element(*self.FILTER_FIRST).get_attribute('value')
        assert actual_name == self.First, f'Expected name: {self.First}, Actual name: {actual_name}'
        #actual_name = self.find_element(*self.FILTER_FIRST).get_attribute('value')
        #assert actual_name in self.FILTER_FIRST, f'Expected name: {self.First}, Actual name: {actual_name}'

    #def filter_products_by_price_range(self, expected_text):
       # actual_text = self.find_element(*self.FILTER_RESULT).text
        #assert actual_text == expected_text,  \
           # f'Error, expected {expected_text} did not match actual {actual_text}'

   # def verify_price_inside_range(self, expected_text):
       # actual_text = self.find_element(*self.FILTER_RESULT).text
        #assert actual_text == expected_text, \
           # f'Error, expected {expected_text} did not match actual {actual_text}'
