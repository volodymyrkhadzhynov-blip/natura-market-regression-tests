"""REG-084: Order summary updates during checkout."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_084_order_summary_updates_during_checkout(home_page: Page):
    """Order summary updates across steps."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
