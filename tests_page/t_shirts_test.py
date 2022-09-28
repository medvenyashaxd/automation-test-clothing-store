import allure

from pages.actions import Actions
from pages.t_shirts_page import TshirtsPage


@allure.suite('Test T-shirts')
class TestTshirts:

    @allure.feature('Test Sleeve T-shirts')
    class TestSleeveTshirts:

        @allure.title('Check sleeve T-shirts')
        def test_card_faded_short_sleeve_tshirts(self, driver):
            url = 'https://automationpractice.com/index.php?id_category=5&controller=category'

            t_shirts_page = TshirtsPage(driver, url)
            t_shirts_page.open()
            added_product_name = t_shirts_page.check_sleeve_t_shirts()

            with allure.step('Checking the item added to the cart and deleting it'):
                product_in_cart = Actions(driver, url).check_shopping_cart_summary()

            assert added_product_name in product_in_cart, 'Added product is not in the cart'
