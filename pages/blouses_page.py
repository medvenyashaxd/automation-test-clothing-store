import random
import allure

from locators.blouses_locators import BlousesLocators
from pages.action import Action


class BlousesPage(Action):
    locator = BlousesLocators()

    @allure.step('Choose_random_color')
    def choose_random_color(self):
        num = random.randint(1, 2)
        if num == 1:
            self.element_is_present(self.locator.BLACK_COLOR).click()
        else:
            self.element_is_present(self.locator.WHITE_COLOR).click()

    @allure.step('Check short_sleeved_blouse')
    def check_short_sleeved_blouse(self):
        with allure.step('Change the overview of product cards'):
            self.element_is_present(self.locator.VIEW_LIST).click()

        with allure.step('Go inside the card'):
            self.element_is_present(self.locator.BUTTON_MORE).click()

        with allure.step('Select product properties'):
            self.select_by_value(self.locator.SIZE, value=f'{random.randint(1, 3)}')
            self.click_random_amount_quantity_up(self.locator.BUTTON_QUANTITY_UP)
            self.choose_random_color()

        self.element_is_present(self.locator.BUTTON_ADD_TO_CARD).click()

        with allure.step('Take the name of the product for comparison'):
            added_product_name = self.element_is_visible(self.locator.PRODUCT_ADDED_NAME).text

        with allure.step('Keep shopping'):
            self.element_is_present(self.locator.BUTTON_CONTINUE_SHOPPING).click()

        with allure.step('Checking the item added to the cart and deleting it'):
            product_in_cart = self.check_shopping_cart_summary()
            assert added_product_name in product_in_cart

        return True
