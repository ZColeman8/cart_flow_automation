from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import logger

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zipcode = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")

    def enter_first_name(self, first_name):
        logger.info("Entering first name")
        field = self.wait.until(EC.element_to_be_clickable(self.first_name))
        field.clear()
        field.send_keys(first_name)
        logger.debug(f"First name entered: {first_name}")

    def enter_last_name(self, last_name):
        logger.info("Entering last name")
        field = self.wait.until(EC.element_to_be_clickable(self.last_name))
        field.clear()
        field.send_keys(last_name)
        logger.debug(f"Last name entered: {last_name}")

    def enter_zipcode(self, zipcode):
        logger.info("Entering zipcode")
        field = self.wait.until(EC.element_to_be_clickable(self.zipcode))
        field.clear()
        field.send_keys(zipcode)
        logger.debug(f"Zipcode entered: {zipcode}")

    def click_continue(self):
        logger.info("Clicking continue button")
        self.wait.until(EC.element_to_be_clickable(self.continue_btn)).click()
        logger.debug("Continue button clicked")

    def fill_checkout_form(self, first_name, last_name, zipcode):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zipcode(zipcode)
        self.click_continue()