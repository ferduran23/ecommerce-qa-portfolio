from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    SEARCH_INPUT = (By.ID, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-button")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-item")
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".product-title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_product(self, product_name):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        search_box.clear()
        search_box.send_keys(product_name)

        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()

    def get_product_titles(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_TITLES)
        )

        return [product.text for product in products]