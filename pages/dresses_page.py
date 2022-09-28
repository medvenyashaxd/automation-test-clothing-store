import random
import allure

from locators.color_locators import ColorLocators
from locators.dresses_locators import DressesLocators
from pages.actions import Actions


class DressesPage(Actions):
    locators_summer_dresses = DressesLocators.PrintedSummerDressLocator
    locators_evening_dresses = DressesLocators.PrintedEveningDressLocator
    locators_casual_dresses = DressesLocators.CasualDressLocator
    color_locators = ColorLocators

    @allure.step('Сhecking a specific dress')
    def check_dresses(self, dress, locator_summer_dresses=locators_summer_dresses, locator_evening_dresses=
                      locators_evening_dresses, locator_casual_dresses=locators_casual_dresses, color_locator=
                      ColorLocators):

        dresses = {'Printed summer dress long':
                       {'title_type_dress': locator_summer_dresses.SUMMER_DRESSES,
                        'button_more': locator_summer_dresses.BUTTON_MORE_PRINTED_SUMMER_DRESS_LONG},

                   'Printed summer dress short':
                       {'title_type_dress': locator_summer_dresses.SUMMER_DRESSES,
                        'button_more': locator_summer_dresses.BUTTON_MORE_PRINTED_SUMMER_DRESS_SHORT},

                   'Printed summer chiffon dress':
                       {'title_type_dress': locator_summer_dresses.SUMMER_DRESSES,
                        'button_more': locator_summer_dresses.BUTTON_MORE_PRINTED_CHIFFON_DRESS},

                   'Printed evening dress straight sleeves':
                       {'title_type_dress': locator_evening_dresses.EVENING_DRESSES,
                        'button_more': locator_evening_dresses.BUTTON_MORE_PRINTED_EVENING_DRESS},

                   'Printed double casual dress':
                       {'title_type_dress': locator_casual_dresses.CASUAL_DRESSES,
                        'button_more': locator_casual_dresses.BUTTON_MORE_CASUAL_DOUBLE_PRINTED_DRESS}}

        RANDOM_NUM = random.randint(1, 4)

        with allure.step('go to product card'):
            self.move_mouse_to_element(self.element_is_visible(locator_summer_dresses.TITLE_DRESSES))
            self.element_is_visible(dresses[dress]['title_type_dress']).click()

        with allure.step('Opening cards in a list'):
            self.element_is_present(locator_summer_dresses.OPEN_FULL_LIST).click()

        with allure.step('Go to the dress and press the more button'):
            self.scroll_to_element(self.element_is_present(dresses[dress]['button_more']))
            self.element_is_present(dresses[dress]['button_more']).click()

        with allure.step('Changing product properties'):
            self.click_random_amount_quantity_up(locator_summer_dresses.BUTTON_QUANTITY_UP)
            self.select_by_value(self.locators_summer_dresses.SIZE, value=f'{random.randint(1, 3)}')

            if dresses[dress] == 'Printed summer dress long':
                if RANDOM_NUM == 1:
                    self.element_is_present(color_locator.COLOR_BLACK).click()
                elif RANDOM_NUM == 2:
                    self.element_is_present(color_locator.COLOR_BLUE).click()
                elif RANDOM_NUM == 3:
                    self.element_is_present(color_locator.COLOR_ORANGE).click()
                else:
                    self.element_is_present(color_locator.COLOR_YELLOW).click()

            elif dresses[dress] == 'Printed summer dress short':
                if RANDOM_NUM == 1 or 2:
                    self.element_is_present(color_locator.COLOR_YELLOW).click()
                else:
                    self.element_is_present(color_locator.COLOR_WHITE).click()

            elif dresses[dress] == 'Printed summer chiffon dress':
                if RANDOM_NUM == 1 or 2:
                    self.element_is_present(color_locator.COLOR_YELLOW).click()
                else:
                    self.element_is_present(color_locator.COLOR_GREEN).click()

            elif dresses[dress] == 'Printed evening dress straight sleeves':
                if RANDOM_NUM == 1 or 2:
                    self.element_is_present(color_locator.COLOR_BEIGE).click()
                else:
                    self.element_is_present(color_locator.COLOR_PINK).click()

            elif dresses[dress] == 'Printed double casual dress':
                self.element_is_present(color_locator.COLOR_ORANGE).click()

        with allure.step('Click on the add to cart button'):
            self.element_is_present(locator_summer_dresses.BUTTON_ADD_TO_CARD).click()

        with allure.step('Take the text from the confirmation message'):
            added_product = self.element_is_visible(locator_summer_dresses.PRODUCT_ADDED_NAME).text

        with allure.step('Continue shopping'):
            self.element_is_present(locator_summer_dresses.BUTTON_CONTINUE_SHOPPING).click()
            self.element_is_present(locator_summer_dresses.CATEGORY_DRESSES).click()

        return added_product
