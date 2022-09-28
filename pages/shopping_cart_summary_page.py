import allure

from locators.shopping_cart_summary_locators import ShoppingCartSummaryLocators
from pages.actions import Actions


class ShoppingCardSummaryPage(Actions):

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
