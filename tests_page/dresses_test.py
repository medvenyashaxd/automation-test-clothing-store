import allure

from pages.dresses_page import DressesPage


@allure.suite('Test dresses')
class TestDresses:

    @allure.feature('Test summer dresses')
    class TestSummerDresses:

        @allure.title('Check summer dresses')
        def test_summer_dresses(self, driver):
            dresses_page = DressesPage(driver, 'https://automationpractice.com/index.php')
            dresses_page.open()
            printed_summer_dress_long = dresses_page.check_dresses('Printed summer dress long')
            printed_summer_dress_short = dresses_page.check_dresses('Printed summer dress short')
            printed_summer_chiffon_dress = dresses_page.check_dresses('Printed summer chiffon dress')

            assert printed_summer_dress_long == 'Printed Summer Dress'
            assert printed_summer_dress_short == 'Printed Summer Dress'
            assert printed_summer_chiffon_dress == 'Printed Chiffon Dress'

    @allure.feature('Test evening dresses')
    class TestEveningDresses:

        @allure.title('Check evening dresses')
        def test_evening_dresses(self, driver):
            dresses_page = DressesPage(driver, 'https://automationpractice.com/index.php')
            dresses_page.open()
            printed_evening_dress_straight_sleeves = dresses_page.check_dresses(
                'Printed evening dress straight sleeves')

            assert printed_evening_dress_straight_sleeves == 'Printed Dress'

    @allure.feature('Test casual dresses')
    class TestCasualDresses:

        @allure.title('Check casual dresses')
        def test_casual_dresses(self, driver):
            dresses_page = DressesPage(driver, 'https://automationpractice.com/index.php')
            dresses_page.open()
            printed_double_casual_printed_dress = dresses_page.check_dresses('Printed double casual dress')

            assert printed_double_casual_printed_dress == 'Printed Dress'
