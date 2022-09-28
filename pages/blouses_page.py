import random
import allure

from locators.blouses_locators import BlousesLocators
from pages.actions import Actions


class BlousesPage(Actions):

    locators = BlousesLocators()

    @allure.step('Choose_random_color')
    def choose_random_color(self, locator=locators):
        num = random.randint(1, 2)
        if num == 1:
            self.element_is_present(locator.BLACK_COLOR).click()
        else:
            self.element_is_present(locator.WHITE_COLOR).click()

    @allure.step('Check short_sleeved_blouse')
    def check_short_sleeved_blouse(self, locator=locators):
        with allure.step('Change the overview of product cards'):
            self.element_is_present(locator.VIEW_LIST).click()

        with allure.step('Go inside the card'):
            self.element_is_present(locator.BUTTON_MORE).click()

        with allure.step('Select product properties'):
            self.select_by_value(locator.SIZE, value=f'{random.randint(1, 3)}')
            self.click_random_amount_quantity_up(locator.BUTTON_QUANTITY_UP)
            self.choose_random_color()

        self.element_is_present(locator.BUTTON_ADD_TO_CARD).click()

        with allure.step('Take the name of the product for comparison'):
            added_product_name = self.element_is_visible(locator.PRODUCT_ADDED_NAME).text

        with allure.step('Keep shopping'):
            self.element_is_present(locator.BUTTON_CONTINUE_SHOPPING).click()

        return added_product_name
