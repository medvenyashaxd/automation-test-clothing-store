import allure

from pages.blouses_page import BlousesPage

@allure.suite('Test blouses')
class TestBlouses:

    @allure.feature('Test shorts sleeved blouse')
    class TestShortSleevedBlouse:

        @allure.title('Check short sleeved blouse')
        def test_short_sleeved_blouse(self, driver):
            sleeved_blouse_page = BlousesPage(driver,
                                            'http://automationpractice.com/index.php?id_category=7&controller=category')
            sleeved_blouse_page.open()

            product_added_name = sleeved_blouse_page.check_short_sleeved_blouse()

            assert product_added_name == 'Blouse'


