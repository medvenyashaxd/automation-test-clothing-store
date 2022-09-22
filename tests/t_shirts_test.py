import allure

from pages.t_shirts_page import TshirtsPage


@allure.suite('Test T-shirts')
class TestTshirts:

    @allure.feature('Test Sleeve T-shirts')
    class TestSleeveTshirts:

        @allure.title('Check sleeve T-shirts')
        def test_card_tshirts(self, driver):
            t_shirts_page = TshirtsPage(driver,
                                            'http://automationpractice.com/index.php?id_category=5&controller=category')
            t_shirts_page.open()
            check_added_out_product = t_shirts_page.check_sleeve_t_shirts()

            assert check_added_out_product == 'Faded Short Sleeve T-shirts'
