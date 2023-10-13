from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open amazon page')
def open_amazon(context):
#    context.driver.get('https://www.amazon.com')
     context.app.main_page.open_main()

@when('Click on Orders')
def click_cart(context):
#     context.driver.find_element(By.ID, 'nav-cart-count-container').click()
    context.app.header.click_signin_popup()


@then('Verify Sign in text is {expected_result}')
def verify_cart_empty(context, expected_result):
    context.app.sign_in_page.verify_signin_opened(expected_result)

@when('Click on shopping cart icon')
def click_on_shopping_cart_icon(context):
    context.app.shopping_cart.click_cart()

@then('Verify cart result is {result}')
def verify_cart_result(context, result):
    context.app.shopping_cart.verify_empty_cart(result)