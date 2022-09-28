from selenium.webdriver.common.by import By


class DressesLocators:
    class PrintedSummerDressLocator:

        TITLE_DRESSES = (By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[2]/a')
        CATEGORY_DRESSES = (By.XPATH, '/html/body/div/div[2]/div/div[1]/a[4]')
        SUMMER_DRESSES = (By.XPATH, '//div[3]/div/div/div[6]/ul/li[2]/ul/li[3]/a')

        BUTTON_MORE_PRINTED_SUMMER_DRESS_LONG = (By.XPATH, '//div[3]/div[2]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]')
        OPEN_FULL_LIST = (By.CSS_SELECTOR, 'i[class="icon-th-list"]')
        BUTTON_QUANTITY_UP = (By.CSS_SELECTOR, 'a[class="btn btn-default button-plus product_quantity_up"]')
        SIZE = (By.CSS_SELECTOR, 'select[id="group_1"]')

        BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, 'p[class="buttons_bottom_block no-print"] button')
        PRODUCT_ADDED_NAME = (By.CSS_SELECTOR, 'span[class="product-name"]')
        BUTTON_CONTINUE_SHOPPING = (By.CSS_SELECTOR, 'span[class="continue btn btn-default button exclusive-medium"]')

        BUTTON_MORE_PRINTED_SUMMER_DRESS_SHORT = (By.XPATH, '//div[2]/ul/li[2]/div/div/div[3]/div/div[2]/a[2]')
        BUTTON_MORE_PRINTED_CHIFFON_DRESS = (By.XPATH, '//div[3]/div[2]/ul/li[3]/div/div/div[3]/div/div[2]/a[2]')

    class PrintedEveningDressLocator:

        EVENING_DRESSES = (By.XPATH, '//div[3]/div/div/div[6]/ul/li[2]/ul/li[2]/a')
        BUTTON_MORE_PRINTED_EVENING_DRESS = (By.XPATH, '//div/div/div[3]/div/div[2]/a[2]')

    class CasualDressLocator:

        CASUAL_DRESSES = (By.XPATH, '//div/div/div[6]/ul/li[2]/ul/li[1]/a')
        BUTTON_MORE_CASUAL_DOUBLE_PRINTED_DRESS = (By.XPATH, '//ul/li/div/div/div[3]/div/div[2]/a[2]')
