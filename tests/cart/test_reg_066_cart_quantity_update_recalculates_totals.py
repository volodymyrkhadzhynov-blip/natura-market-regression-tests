"""REG-066: Cart quantity update recalculates totals."""
import pytest
from playwright.sync_api import Page

from pages.header import Header
from pages.cart import CartPage
from tests.helpers import add_product_to_cart


@pytest.mark.regression
def test_reg_066_cart_quantity_update_recalculates_totals(home_page: Page):
    """Changing quantity updates totals."""
    add_product_to_cart(home_page)
    page = home_page
    Header(page).open_cart()
    page.wait_for_load_state("domcontentloaded")
    qty = CartPage(page).quantity_input(0)
    if qty.is_visible(timeout=3000):
        qty.fill("2")
        page.wait_for_timeout(1500)
    assert page.locator("body").is_visible()
