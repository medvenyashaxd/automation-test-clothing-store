import allure

from pages.dresses_page import DressesPage
from pages.shopping_cart_summary_page import ShoppingCardSummaryPage


@allure.suite('Test dresses')
class TestDresses:

    @allure.feature('Test summer dresses')
    class TestSummerDresses:

        @allure.title('Check summer dresses')
        def test_summer_dresses(self, driver):
            url = 'https://automationpractice.com/index.php'

            dresses_page = DressesPage(driver, url)
            dresses_page.open()
            printed_summer_dress_long = dresses_page.check_dresses('Printed summer dress long')
            printed_summer_dress_short = dresses_page.check_dresses('Printed summer dress short')
            printed_summer_chiffon_dress = dresses_page.check_dresses('Printed summer chiffon dress')

            with allure.step('Checking the item added to the cart and deleting it'):
                summary_page = ShoppingCardSummaryPage(driver, url)
                product_in_cart = summary_page.check_shopping_cart_summary()

            assert printed_summer_dress_long in product_in_cart
            assert printed_summer_dress_short in product_in_cart
            assert printed_summer_chiffon_dress in product_in_cart

    @allure.feature('Test evening dresses')
    class TestEveningDresses:

        @allure.title('Check evening dresses')
        def test_evening_dresses(self, driver):
            url = 'https://automationpractice.com/index.php'

            dresses_page = DressesPage(driver, url)
            dresses_page.open()
            printed_evening_dress_straight_sleeves = dresses_page.check_dresses(
                'Printed evening dress straight sleeves')

            with allure.step('Checking the item added to the cart and deleting it'):
                summary_page = ShoppingCardSummaryPage(driver, url)
                product_in_cart = summary_page.check_shopping_cart_summary()

            assert printed_evening_dress_straight_sleeves in product_in_cart

    @allure.feature('Test casual dresses')
    class TestCasualDresses:

        @allure.title('Check casual dresses')
        def test_casual_dresses(self, driver):
            url = 'https://automationpractice.com/index.php'

            dresses_page = DressesPage(driver, url)
            dresses_page.open()
            printed_double_casual_printed_dress = dresses_page.check_dresses('Printed double casual dress')

            with allure.step('Checking the item added to the cart and deleting it'):
                summary_page = ShoppingCardSummaryPage(driver, url)
                product_in_cart = summary_page.check_shopping_cart_summary()

            assert printed_double_casual_printed_dress in product_in_cart
