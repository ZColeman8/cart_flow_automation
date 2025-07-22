from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import logger
from selenium.common.exceptions import TimeoutException  # Add this import

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_product_in_cart(self, product_name):
        xpath = f"//div[@class='inventory_item_name' and text()='{product_name}']"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            logger.info(f"Product '{product_name}' is present in the cart.")
            return True
        except TimeoutException:
            logger.warning(f"Product '{product_name}' is NOT found in the cart.")
            return False

    def click_checkout_button(self):
        logger.info("Clicking the checkout button")
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()
        logger.debug("Checkout button clicked")
