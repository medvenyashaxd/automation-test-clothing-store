import random
import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from locators.shopping_cart_summary_locators import ShoppingCartSummaryLocators


class Actions:
    def __init__(self, _driver, _url):
        self.driver = _driver
        self.url = _url

    @allure.step('Gets link')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Finds a visible element')
    def element_is_visible(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step('Finds visible elements')
    def element_are_visible(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step('Finds a present element')
    def element_is_present(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    @allure.step('Finds a present elements')
    def elements_are_presents(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    @allure.step('Moves the mouse cursor an element')
    def move_mouse_to_element(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()

    @allure.step('Moves screen attention to an element')
    def scroll_to_element(self, locator):
        action = ActionChains(self.driver)
        action.scroll_to_element(locator).perform()

    @allure.step('Moves screen attention to an element')
    def scroll_to_element2(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    @allure.step('Selects the specified value from the provided values')
    def select_by_value(self, locator, value):
        action = Select(self.element_is_present(locator))
        action.select_by_value(value)

    @allure.step('Press random amount quantity up ')
    def click_random_amount_quantity_up(self, locator):
        number_of_clicks = random.randint(1, 2)
        while number_of_clicks != 0:
            self.element_is_present(locator).click()
            number_of_clicks -= 1

    locators = ShoppingCartSummaryLocators()

    @allure.step('Go to the summary cart, check the added product and remove it from the cart')
    def check_shopping_cart_summary(self, locator=locators):
        with allure.step('Go to the summary cart'):
            self.move_mouse_to_element(self.element_is_visible(locator.TITLE_CART_SUMMARY))
            self.move_mouse_to_element(self.element_is_visible(locator.CHECK_OUT))
            self.element_is_present(locator.CHECK_OUT).click()

        with allure.step('Check the added product'):
            products_added_in_cart_summary = self.elements_are_presents(locator.PRODUCT_NAME)
            product_name = []
            for name in products_added_in_cart_summary:
                text = name.text
                product_name.append(text)

        with allure.step('remove product from the cart'):
            buttons_delete = self.elements_are_presents(locator.BUTTON_DELETE)
            for button in buttons_delete:
                button.click()

        with allure.step('Confirmation that the basket is empty'):
            delete_notification = self.element_is_visible(locator.DELETE_NOTIFICATION).text

        assert delete_notification == 'Your shopping cart is empty.', 'Cart not cleared'

        return product_name
