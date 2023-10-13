from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# create a new Chrome browser instance
service = Service(executable_path='<provide your absolute path>')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

# Input search text
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

# Click on search btn
driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"table"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
print('Test case passed')

driver.quit()
 35 changes: 35 additions & 0 deletions35
locators.py
Viewed
@@ -0,0 +1,35 @@
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# create a new Chrome browser instance
service = Service(executable_path='<provide your absolute path>')
driver = webdriver.Chrome(service=service)


# By ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'nav-cart-count')

# By XPATH

# Tag and attribute
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

# Multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

# By Xpath, text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# Any tag = *
driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")

# Contains
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(text(), 't Seller') and @class='nav-a  ']")

# //parent[...]//child[...]
driver.find_element(By.XPATH, "//div[@id='nav-belt']//input[@placeholder='Search Amazon']")