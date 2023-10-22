from pages.base_page import Page
from time import sleep


class MainPage(Page):

    def open_main(self):
        self.driver.get('https://soft.reelly.io/')

        sleep(2)
        self.driver.refresh()



