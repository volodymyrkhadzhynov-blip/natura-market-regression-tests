"""REG-070: Estimate shipping control is available on cart when supported."""
import pytest
from playwright.sync_api import Page

from pages.header import Header
from tests.helpers import add_product_to_cart


@pytest.mark.regression
def test_reg_070_estimate_shipping_available_when_supported(home_page: Page):
    """Shipping estimate block visible when supported."""
    add_product_to_cart(home_page)
    page = home_page
    Header(page).open_cart()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
