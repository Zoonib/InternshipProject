from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_url(self, end_url=''):
        url = f'https://soft.reelly.io/{end_url}'
        self.driver.get(url)
        #logger.info(f'Openning URL {url}')
        sleep(2)
        self.driver.refresh()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text: str, *locator):
        e = self.find_element(*locator)
        e.send_keys(text)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text in expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error, expected partial text {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_part_of_url):
        self.wait.until(EC.url_contains(expected_part_of_url))
        sleep(4)