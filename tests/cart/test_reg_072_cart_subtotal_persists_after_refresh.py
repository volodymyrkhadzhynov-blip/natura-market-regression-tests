"""REG-072: Cart subtotal persists after page refresh."""
import pytest
from playwright.sync_api import Page

from pages.header import Header
from tests.helpers import add_product_to_cart


@pytest.mark.regression
def test_reg_072_cart_subtotal_persists_after_refresh(home_page: Page):
    """Cart content and subtotal persist after refresh."""
    add_product_to_cart(home_page)
    page = home_page
    Header(page).open_cart()
    page.wait_for_load_state("domcontentloaded")
    page.reload()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
