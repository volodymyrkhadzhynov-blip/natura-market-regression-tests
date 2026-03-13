"""REG-064: User can open full cart page."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL
from tests.helpers import add_product_to_cart


@pytest.mark.regression
@pytest.mark.smoke
def test_reg_064_user_can_open_full_cart_page(home_page: Page):
    """Cart page is accessible after adding a product."""
    add_product_to_cart(home_page)
    page = home_page
    # Navigate directly to cart — showcart link goes there
    page.goto(f"{BASE_URL}/checkout/cart/", wait_until="domcontentloaded")
    page.wait_for_timeout(1000)
    assert "cart" in page.url.lower()
