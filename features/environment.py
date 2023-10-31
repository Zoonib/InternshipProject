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

    # service = Service(executable_path='/Users/zoonib/Downloads/InternshipProject/chromedriver.exe'
    # # context.driver = webdriver.Chrome(service=service)
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    mobile_emulation = {

        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}

    options = webdriver.ChromeOptions()

    options.add_experimental_option("mobileEmulation", mobile_emulation)

    context.driver = webdriver.Chrome(options=options)



    ## HEADLESS MODE ##
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(
      #  options=options,
      #  service=service
   # )

    ### BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
   # bs_user = 'zoonibutt_LQMHgj'
   # bs_key = 'mTJJkLGA4xqQaocpYQ'
   # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

   # options = Options()
    #bstack_options = {
     #  'os': 'Windows',
      #'osVersion': '10',
    #    'browserName': 'Firefox',
    #    'sessionName': 'scenario_name'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

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