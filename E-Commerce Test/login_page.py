from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".message-error")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text