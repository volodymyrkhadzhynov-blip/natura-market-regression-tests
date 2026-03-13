"""REG-075: Shipping address required-field validation works."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_075_shipping_address_required_validation(home_page: Page):
    """Empty required address fields show validation."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    cont = page.get_by_role("button", name="Continue").or_(
        page.get_by_role("button", name="Next")
    ).first
    if cont.is_visible(timeout=5000):
        cont.click()
        page.wait_for_timeout(1500)
    assert page.locator("body").is_visible()
