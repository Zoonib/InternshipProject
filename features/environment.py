from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.service import Service
#from support.logger import logger
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




def browser_init(context):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    #service = Service(executable_path='/Users/zoonib/Downloads/InternshipProject/chromedriver.exe'
    # context.driver = webdriver.Chrome(service=service)
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    ## HEADLESS MODE ##
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )


    context.driver.set_window_size(1920, 1080)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()