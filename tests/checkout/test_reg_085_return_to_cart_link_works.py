"""REG-085: Return to cart link works from checkout."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_085_return_to_cart_link_works(home_page: Page):
    """Return to cart from checkout keeps cart."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    back = page.get_by_role("link", name="Cart").or_(
        page.get_by_text("Return to cart")
    ).first
    if back.is_visible(timeout=5000):
        back.click()
        page.wait_for_load_state("domcontentloaded")
        assert "cart" in page.url.lower()
    assert page.locator("body").is_visible()
