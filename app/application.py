from pages.main_page import MainPage
# from pages.header import Header
# from pages.search_result_page import SearchResultPage
# from pages.sign_in_page import SignInPage
# from pages.shopping_cart import ShoppingCart


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.log_in_page= logInpage(driver)
        self.click_left_side_menu = clickleftsidemenu(driver)
        self.verify_right_page_opens = verifyrightpageopens(driver)
        self.filter_products_by_price_range = filterproductsbypricerange(driver)
        self.verify_price_inside_range = verifypriceinsiderange(driver)