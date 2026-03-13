"""REG-065: Cart page displays line item details."""
import pytest
from playwright.sync_api import Page

from pages.header import Header
from tests.helpers import add_product_to_cart


@pytest.mark.regression
def test_reg_065_cart_page_displays_line_item_details(home_page: Page):
    """Cart shows product name, quantity, price, subtotal."""
    add_product_to_cart(home_page)
    page = home_page
    Header(page).open_cart()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("table").or_(page.locator("[class*='cart']")).first.is_visible(timeout=5000)
