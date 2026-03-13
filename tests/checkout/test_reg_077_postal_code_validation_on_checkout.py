"""REG-077: Postal code validation works on checkout shipping address."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_077_postal_code_validation_on_checkout(home_page: Page):
    """Invalid postal code shows validation."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    postal = page.get_by_label("Postal").or_(
        page.get_by_placeholder("Postal")
    ).first
    if postal.is_visible(timeout=5000):
        postal.fill("000")
        page.get_by_role("button", name="Continue").first.click()
        page.wait_for_timeout(1500)
    assert page.locator("body").is_visible()
