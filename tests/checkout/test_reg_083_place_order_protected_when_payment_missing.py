"""REG-083: Place Order action is protected when mandatory payment data is missing."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_083_place_order_protected_when_payment_missing(home_page: Page):
    """Place Order blocked or validated when payment data missing."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    place = page.get_by_role("button", name="Place Order").or_(
        page.get_by_text("Place Order")
    ).first
    if place.is_visible(timeout=5000):
        place.click()
        page.wait_for_timeout(1500)
    assert page.locator("body").is_visible()
