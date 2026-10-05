from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "button.add-to-cart-button"
    )

    CART_LINK = (
        By.CSS_SELECTOR,
        "a.ico-cart"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()