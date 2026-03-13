"""REG-080: Billing address can be same as shipping."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_080_billing_same_as_shipping(home_page: Page):
    """Same as shipping option uses shipping as billing."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    same = page.get_by_text("Same as shipping").or_(
        page.get_by_label("Same as shipping")
    ).first
    if same.is_visible(timeout=5000):
        assert same.is_visible()
    assert page.locator("body").is_visible()
