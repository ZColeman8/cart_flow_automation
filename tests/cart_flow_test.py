from src.pages.sign_in_page import SignInPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.checkout_finalize_page import FinalizeCheckoutPage
from src.utils.logger import logger

def test_cart_flow(driver):
    logger.info("Starting cart flow test")
    driver.get("https://www.saucedemo.com/")

    sign_in_page = SignInPage(driver)
    sign_in_page.login("standard_user")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    logger.debug("Product added: Sauce Labs Backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_product_in_cart("Sauce Labs Backpack"), "Backpack not found in cart"
    cart_page.click_checkout_button()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Zach", "Coleman", "12345")
    logger.debug("Checkout details: Zach Coleman, 12345")

    finalize_checkout_page = FinalizeCheckoutPage(driver)
    finalize_checkout_page.click_finalize_button()
    assert finalize_checkout_page.is_order_complete(), "Order confirmation not displayed"
    logger.info("Test completed successfully")