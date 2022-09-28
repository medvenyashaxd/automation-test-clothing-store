import random

from selenium.webdriver.common.by import By


class TshirtsLocators:

    SLEEVE_T_SHIRTS = (By.CSS_SELECTOR, 'img[alt="Faded Short Sleeve T-shirts"]')
    BUTTON_MORE = (By.CSS_SELECTOR, 'a[title="View"]')
    QUANTITY_UP = (By.CSS_SELECTOR, 'a[data-field-qty="qty"][class="btn btn-default button-plus product_quantity_up"]')
    SIZE = (By.CSS_SELECTOR, 'select[id="group_1"]')
    COLOR = (By.CSS_SELECTOR, f'a[id="color_{random.randint(13, 14)}"]')

    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, 'p[class="buttons_bottom_block no-print"] button')
    CHECK_PRODUCT_SHOPPING_CARD = (By.CSS_SELECTOR, 'span[id="layer_cart_product_title"]')
    BUTTON_CONTINUE_SHOPPING = (By.CSS_SELECTOR, 'span[class="continue btn btn-default button exclusive-medium"]')
