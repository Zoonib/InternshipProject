from behave import given, when, then
from time import sleep


@given('Open main page on mobile')
def open_reelly(context):
    context.app.main_page.open_main()
    sleep(2)

@when('Log in to the page on mobile')
def log_in_page(context):
        sleep(2)
        context.app.log_in_page.email_log_in()
        context.app.log_in_page.password_log_in()
        context.app.log_in_page.continue_button()
        sleep(3)

# @when('Click on Secondary option at the left side menu on mobile')
# def click_left_side_menu(context):
#     context.app.page_opens.click_left_side_menu()

@when('Click on Filter button')
def filter_products_by_price_range(context):
    context.app.mobile.filter_btn()
    sleep(2)


@when('Input amount 1200000 to 2000000')
def input_amount(context):
    sleep(2)
    context.app.filter_products.filter_first()
    context.app.filter_products.filter_second()

@then ('Verify amount 1200000 to 200000')
def verify_price_range(context):
    context.app.filter_products.verify_info()
