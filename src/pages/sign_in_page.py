from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import logger

class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def enter_username(self, username):
        logger.info("Entering username")
        field = self.wait.until(EC.element_to_be_clickable(self.username_input))
        field.clear()
        field.send_keys(username)
        logger.debug(f"Username used: {username}")

    def enter_password(self, password="secret_sauce"):
        logger.info("Entering password")
        field = self.wait.until(EC.element_to_be_clickable(self.password_input))
        field.clear()
        field.send_keys(password)
        logger.debug(f"Password entered")

    def click_sign_in(self):
        logger.info("Clicking Sign in")
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
        logger.debug("Log in button clicked")

    def login(self, username, password="secret_sauce"):
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()