import random
import allure

from locators.t_shirts_locators import TshirtsLocators
from pages.action import Action


class TshirtsPage(Action):
    locator = TshirtsLocators

    @allure.step('Check sleeve t shirts')
    def check_sleeve_t_shirts(self):
        with allure.step('Define a product card'):
            card_sleeve_tshirts = self.element_is_present(self.locator.SLEEVE_T_SHIRTS)

        with allure.step('Move to the product'):
            self.scroll_to_element2(card_sleeve_tshirts)
            self.move_mouse_to_element(card_sleeve_tshirts)

        self.element_is_present(self.locator.BUTTON_MORE).click()

        with allure.step('Select product properties'):
            self.click_random_amount_quantity_up(self.locator.QUANTITY_UP)
            self.select_by_value(self.locator.SIZE, value=f'{random.randint(1, 3)}')
            self.element_is_present(self.locator.COLOR).click()

        self.element_is_present(self.locator.BUTTON_ADD_TO_CARD).click()

        with allure.step('Take the name of the product for comparison'):
            added_product = self.element_is_visible(self.locator.CHECK_PRODUCT_SHOPPING_CARD).text

        with allure.step('Keep shopping'):
            self.element_is_present(self.locator.BUTTON_CONTINUE_SHOPPING).click()

        return added_product
