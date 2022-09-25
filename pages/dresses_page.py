import random
import time
import allure

from locators.dresses_locators import Dresses
from pages.action import Action


class DressesPage(Action):
    locator_summer_dresses = Dresses.PrintedSummerDressLocator
    locator_evening_dresses = Dresses.PrintedEveningDressLocator
    locator_casual_dresses = Dresses.CasualDressLocator

    @allure.step('Сhecking a specific dress')
    def check_dresses(self, dress):
        dresses = {'Printed summer dress long':
                       {'title_type_dress': self.locator_summer_dresses.SUMMER_DRESSES,
                        'button_more': self.locator_summer_dresses.BUTTON_MORE_PRINTED_SUMMER_DRESS_LONG},

                   'Printed summer dress short':
                       {'title_type_dress': self.locator_summer_dresses.SUMMER_DRESSES,
                        'button_more': self.locator_summer_dresses.BUTTON_MORE_PRINTED_SUMMER_DRESS_SHORT},

                   'Printed summer chiffon dress':
                       {'title_type_dress': self.locator_summer_dresses.SUMMER_DRESSES,
                        'button_more': self.locator_summer_dresses.BUTTON_MORE_PRINTED_CHIFFON_DRESS},

                   'Printed evening dress straight sleeves':
                       {'title_type_dress': self.locator_evening_dresses.EVENING_DRESSES,
                        'button_more': self.locator_evening_dresses.BUTTON_MORE_PRINTED_EVENING_DRESS},

                   'Printed double casual dress':
                       {'title_type_dress': self.locator_casual_dresses.CASUAL_DRESSES,
                        'button_more': self.locator_casual_dresses.BUTTON_MORE_CASUAL_DOUBLE_PRINTED_DRESS}}

        RANDOM_NUM = random.randint(1, 4)

        with allure.step('go to product card'):
            self.move_mouse_to_element(self.element_is_present(self.locator_summer_dresses.TITLE_DRESSES))
            self.element_is_present(dresses[dress]['title_type_dress']).click()

        with allure.step('Opening cards in a list'):
            self.element_is_present(self.locator_summer_dresses.OPEN_FULL_LIST).click()

        with allure.step('Go to the dress and press the more button'):
            self.scroll_to_element(self.element_is_present(dresses[dress]['button_more']))
            self.element_is_present(dresses[dress]['button_more']).click()

        with allure.step('Changing product properties'):
            self.click_random_amount_quantity_up(self.locator_summer_dresses.BUTTON_QUANTITY_UP)
            self.select_by_value(self.locator_summer_dresses.SIZE, value=f'{random.randint(1, 3)}')

            if dresses[dress] == 'Printed summer dress long':
                if RANDOM_NUM == 1:
                    self.element_is_present(self.locator_summer_dresses.COLOR_BLACK).click()
                elif RANDOM_NUM == 2:
                    self.element_is_present(self.locator_summer_dresses.COLOR_BLUE).click()
                elif RANDOM_NUM == 3:
                    self.element_is_present(self.locator_summer_dresses.COLOR_ORANGE).click()
                else:
                    self.element_is_present(self.locator_summer_dresses.COLOR_YELLOW).click()

            elif dresses[dress] == 'Printed summer dress short':
                if RANDOM_NUM == 1 or 2:
                    self.element_is_present(self.locator_summer_dresses.COLOR_YELLOW).click()
                else:
                    self.element_is_present(self.locator_summer_dresses.COLOR_WHITE).click()

            elif dresses[dress] == 'Printed summer chiffon dress':
                if RANDOM_NUM == 1 or 2:
                    self.element_is_present(self.locator_summer_dresses.COLOR_YELLOW).click()
                else:
                    self.element_is_present(self.locator_summer_dresses.COLOR_GREEN).click()

            elif dresses[dress] == 'Printed evening dress straight sleeves':
                if RANDOM_NUM == 1 or 2:
                    self.element_is_present(self.locator_summer_dresses.COLOR_BEIGE).click()
                else:
                    self.element_is_present(self.locator_summer_dresses.COLOR_PINK).click()

            elif dresses[dress] == 'Printed double casual dress':
                self.element_is_present(self.locator_summer_dresses.COLOR_ORANGE).click()

        with allure.step('Click on the add to cart button'):
            self.element_is_present(self.locator_summer_dresses.BUTTON_ADD_TO_CARD).click()

        with allure.step('Take the text from the confirmation message'):
            added_product = self.element_is_visible(self.locator_summer_dresses.PRODUCT_ADDED_NAME).text

        with allure.step('Continue shopping'):
            self.element_is_present(self.locator_summer_dresses.BUTTON_CONTINUE_SHOPPING).click()

            time.sleep(1)

        return added_product
