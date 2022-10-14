import allure
import pytest

from selenium import webdriver
from datetime import datetime


@pytest.fixture(scope='function')
def driver():
    driver_path = \
        r'C:\Users\xmedv\PycharmProjects\chromedriver.exe'

    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()

    yield driver

    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot{datetime.today()}', attachment_type=allure.attachment_type.PNG)

    driver.quit()
