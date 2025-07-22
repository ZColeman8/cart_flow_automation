from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import logger
from selenium.common.exceptions import TimeoutException  # Add this import

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_product_displayed(self, product_name):
        xpath = f"//div[@class='inventory_item'][.//div[text()='{product_name}']]"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            logger.info(f"Product '{product_name}' is displayed on the inventory page.")
            return True
        except TimeoutException:
            logger.warning(f"Product '{product_name}' is NOT displayed on the inventory page.")
            return False

    def add_product_to_cart_by_name(self, product_name):
        logger.info(f"Adding '{product_name}' to cart")
        xpath = f"//div[@class='inventory_item'][.//div[text()='{product_name}']]//button"
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        add_button.click()
        logger.debug(f"'{product_name}' added to cart")

    def go_to_cart(self):
        logger.info("Navigating to cart")
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()
        logger.debug("Clicked cart icon")
