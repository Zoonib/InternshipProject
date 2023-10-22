from selenium.webdriver.common.by import By
from pages.base_page import Page


class FilterResultPage(Page):
    FILTER_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')

    def filter_products_by_price_range(self, expected_text):
        actual_text = self.find_element(*self.FILTER_RESULT).text
        assert actual_text == expected_text,  \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_price_inside_range(self, expected_text):
        actual_text = self.find_element(*self.FILTER_RESULT).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'
