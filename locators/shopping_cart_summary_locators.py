from selenium.webdriver.common.by import By


class ShoppingCartSummaryLocators:

    BUTTON_DELETE = (By.CSS_SELECTOR, 'i[class="icon-trash"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'p[class="product-name"]')
    TITLE_CART_SUMMARY = (By.CSS_SELECTOR, 'a[title="View my shopping cart"]')
    CHECK_OUT = (By.CSS_SELECTOR, 'a[title="Check out"]')
    DELETE_NOTIFICATION = (By.CSS_SELECTOR, 'p[class="alert alert-warning"]')

