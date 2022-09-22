from datetime import datetime

import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver_path = \
        r'C:\Users\xmedv\PycharmProjects\webdriver\.wdm\drivers\chromedriver\win32\105.0.5195\chromedriver.exe'

    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()

    yield driver

    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot{datetime.today()}', attachment_type=allure.attachment_type.PNG)

    driver.quit()
