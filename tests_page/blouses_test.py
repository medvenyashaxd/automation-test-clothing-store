import allure

from pages.actions import Actions
from pages.blouses_page import BlousesPage


@allure.suite('Test blouses')
class TestBlouses:

    @allure.feature('Test shorts sleeved blouse')
    class TestShortSleevedBlouse:

        @allure.title('Check short sleeved blouse')
        def test_short_sleeved_blouse(self, driver):
            url = 'https://automationpractice.com/index.php?id_category=7&controller=category'

            sleeved_blouse_page = BlousesPage(driver, url)
            sleeved_blouse_page.open()
            added_product_name = sleeved_blouse_page.check_short_sleeved_blouse()

            with allure.step('Checking the item added to the cart and deleting it'):
                product_in_cart = Actions(driver, url).check_shopping_cart_summary()

            assert added_product_name in product_in_cart, 'Added product is not in the cart'

