@Given('Open the main page')
def Open_masin_page(context):
    context.driver.find_element.click()
    sleep(2)


@When ('Log in to the page')
def Log_in_page(context, expected_result):
    actual_result = context.driver.find_element.text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.search_result_page.verify_search_result(expected_result)

@And ('Click on Secondary option at the left side menu.')
def Click_leftside_menu(context):
@then('Verify the right page opens')
def verify_rightpage_opens(context):

@And ('Filter the products by price range from 1200000 to 2000000.')
def Filter_Products_by_price_range(context):

@Then ('Verify the price in all cards is inside the range (1200000 - 2000000).')
def Verify_price_inside_range(context):