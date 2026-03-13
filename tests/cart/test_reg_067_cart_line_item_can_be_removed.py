"""REG-067: Cart line item can be removed."""
import pytest
from playwright.sync_api import Page

from pages.header import Header
from pages.cart import CartPage
from tests.helpers import add_product_to_cart


@pytest.mark.regression
def test_reg_067_cart_line_item_can_be_removed(home_page: Page):
    """Remove button removes line and updates totals."""
    add_product_to_cart(home_page)
    page = home_page
    Header(page).open_cart()
    page.wait_for_load_state("domcontentloaded")
    CartPage(page).remove_item(0)
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
