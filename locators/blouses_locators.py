from selenium.webdriver.common.by import By


class BlousesLocators:

    VIEW_LIST = (By.CSS_SELECTOR, 'i[class="icon-th-list"]')
    BUTTON_MORE = (By.CSS_SELECTOR, 'a[class="button lnk_view btn btn-default"]')
    BUTTON_QUANTITY_UP = (By.CSS_SELECTOR, 'a[class="btn btn-default button-plus product_quantity_up"]')
    SIZE = (By.CSS_SELECTOR, 'select[id="group_1"]')
    BLACK_COLOR = (By.CSS_SELECTOR, 'a[id="color_11"]')
    WHITE_COLOR = (By.CSS_SELECTOR, 'a[id="color_8"]')
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, 'p[class="buttons_bottom_block no-print"] button')
    PRODUCT_ADDED_NAME = (By.CSS_SELECTOR, 'span[class="product-name"]')
    BUTTON_CONTINUE_SHOPPING = (By.CSS_SELECTOR, 'span[class="continue btn btn-default button exclusive-medium"]')
