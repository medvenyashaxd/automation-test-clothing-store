import allure

from pages.t_shirts_page import TshirtsPage


@allure.suite('Test T-shirts')
class TestTshirts:

    @allure.feature('Test Sleeve T-shirts')
    class TestSleeveTshirts:

        @allure.title('Check sleeve T-shirts')
        def test_card_faded_short_sleeve_tshirts(self, driver):
            t_shirts_page = TshirtsPage(driver,
                                            'http://automationpractice.com/index.php?id_category=5&controller=category')
            t_shirts_page.open()
            item_added_to_cart_and_checked = t_shirts_page.check_sleeve_t_shirts()

            assert item_added_to_cart_and_checked is True
