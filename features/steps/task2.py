from behave import given, when, then
from time import sleep


@given('Open the main page')
def Open_main(context):
    context.app.main_page.open_main('sign-up')
    sleep(2)


@when ('Log in to the page')
def log_in_page(context):
    context.app.log_in_page.open_loginpage('LogIn')

@when ('Click on Secondary option at the left side menu.')
def click_left_side_menu(context):
    context.app.click_left_side_menu.self.click(*self.NAV_ORDERS)
@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.verify_right_page_opens.open_verifyrightpageopens('right right side page opens')

@then ('Filter the products by price range from 1200000 to 2000000.')
def filter_products_by_price_range(context):
    context.app.filter_products_by_price_range.open_filterproductsbypricerange('filter products by price range')

@then ('Verify the price in all cards is inside the range (1200000 - 2000000).')
def verify_price_inside_range(context):
    context.app.verify_price_inside_range.open_verifypriceinsiderange('Verify price inside range')