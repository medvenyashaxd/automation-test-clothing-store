import random
import time
import allure

from locators.t_shirts_locators import TshirtsLocators
from pages.action import Action


class TshirtsPage(Action):
    locator = TshirtsLocators

    @allure.step('Press random amount quantity up ')
    def click_random_amount_quantity_up(self):
        number_of_clicks = random.randint(1, 2)
        while number_of_clicks != 0:
            self.element_is_present(self.locator.QUANTITY_UP).click()
            number_of_clicks -= 1

    @allure.step('Check sleeve t shirts')
    def check_sleeve_t_shirts(self):
        with allure.step('Define a product card'):
            card_sleeve_tshirts = self.element_is_present(self.locator.SLEEVE_T_SHIRTS)

        with allure.step('Move to the product'):
            self.scroll_to_element2(card_sleeve_tshirts)
            self.move_mouse_to_element(card_sleeve_tshirts)

        self.element_is_present(self.locator.BUTTON_MORE).click()

        with allure.step('Select product properties'):
            self.click_random_amount_quantity_up()
            self.select_by_value(self.locator.SIZE, value=f'{random.randint(1, 3)}')
            self.element_is_present(self.locator.COLOR).click()

        self.element_is_present(self.locator.BUTTON_ADD_TO_CARD).click()
        time.sleep(15)
        with allure.step('Take the name of the product for comparison'):
            added_product = self.element_is_visible(self.locator.CHECK_PRODUCT_SHOPPING_CARD).text

        with allure.step('Keep shopping'):
            self.element_is_present(self.locator.BUTTON_CONTINUE_SHOPPING).click()

        return added_product
