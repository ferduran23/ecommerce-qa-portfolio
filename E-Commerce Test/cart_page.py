from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item-row")
    REMOVE_CHECKBOXES = (
        By.CSS_SELECTOR,
        "input[name='removefromcart']"
    )
    QUANTITY_INPUT = (
        By.CSS_SELECTOR,
        ".qty-input"
    )
    UPDATE_CART_BUTTON = (
        By.CSS_SELECTOR,
        "button[name='updatecart']"
    )
    SUBTOTAL = (
        By.CSS_SELECTOR,
        ".product-price"
    )
    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        "button.checkout-button"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def remove_first_product(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_CHECKBOXES)
        )

        checkbox.click()

        self.wait.until(
            EC.element_to_be_clickable(self.UPDATE_CART_BUTTON)
        ).click()

    def change_quantity(self, quantity):
        quantity_field = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT)
        )

        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

        self.wait.until(
            EC.element_to_be_clickable(self.UPDATE_CART_BUTTON)
        ).click()

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()