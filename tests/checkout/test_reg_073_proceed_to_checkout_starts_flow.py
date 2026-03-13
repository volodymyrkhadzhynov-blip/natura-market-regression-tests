"""REG-073: Proceed to Checkout starts checkout flow."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_073_proceed_to_checkout_starts_flow(home_page: Page):
    """Proceed to Checkout opens checkout."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    assert "checkout" in page.url.lower() or page.get_by_text("Shipping").or_(
        page.get_by_label("Email")
    ).first.is_visible(timeout=10000)
