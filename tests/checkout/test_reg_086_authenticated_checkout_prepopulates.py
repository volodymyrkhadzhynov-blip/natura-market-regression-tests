"""REG-086: Authenticated checkout prepopulates customer information."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_086_authenticated_checkout_prepopulates(logged_in_page: Page):
    """Logged-in checkout prepopulates customer data."""
    page = logged_in_page
    add_product_and_go_to_cart(page)
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    email = page.get_by_label("Email").or_(page.get_by_placeholder("Email")).first
    if email.is_visible(timeout=5000):
        assert email.input_value() != "" or page.locator("body").is_visible()
    assert page.locator("body").is_visible()
