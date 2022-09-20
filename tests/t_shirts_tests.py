from pages.t_shirts_page import TshirtsPage


class TestTshirts:

    class TestSleeveTshirts:

        def test_card_tshirts(self, driver):
            t_shirts_page = TshirtsPage(driver,
                                            'http://automationpractice.com/index.php?id_category=5&controller=category')
            t_shirts_page.open()