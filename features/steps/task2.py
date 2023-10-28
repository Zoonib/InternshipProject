from behave import given, when, then
from time import sleep


@given('Open main page')
def open_reelly(context):
    context.app.main_page.open_main()
    sleep(2)


@when('Log in to the page')
def log_in_page(context):
    sleep(2)
    context.app.log_in_page.email_log_in()
    context.app.log_in_page.password_log_in()
    context.app.log_in_page.continue_button()
    sleep(3)


@when('Click on Secondary option at the left side menu.')
def click_left_side_menu(context):
    context.app.page_opens.click_left_side_menu()
@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.page_opens.verify_right_page_open()

@then ('Filter the products by price range from 1200000 to 2000000.')
def filter_products_by_price_range(context):
    context.app.filter_products.filter_btn()
    sleep(2)
    context.app.filter_products.filter_first()
    context.app.filter_products.filter_second()

@then ('Verify the price in all cards is inside the range 1200000 to 2000000.')
def verify_price_inside_range(context):
    context.app.filter_products.verify_info()