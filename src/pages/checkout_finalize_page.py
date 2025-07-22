from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import logger
from selenium.common.exceptions import TimeoutException

class FinalizeCheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_finalize_button(self):
        logger.info("Finalizing checkout")
        finalize_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        finalize_btn.click()
        logger.debug("Checkout finalized")

    def is_order_complete(self):
        try:
            confirmation = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
            return "Thank you" in confirmation.text
        except TimeoutException:
            logger.error("Order confirmation not found.")
            return False