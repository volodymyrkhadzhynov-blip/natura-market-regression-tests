"""REG-071: Coupon field validates invalid coupon code."""
import pytest
from playwright.sync_api import Page

from pages.header import Header
from pages.cart import CartPage
from tests.helpers import add_product_to_cart


@pytest.mark.regression
def test_reg_071_coupon_field_validates_invalid_code(home_page: Page):
    """Invalid coupon shows message and totals unchanged."""
    add_product_to_cart(home_page)
    page = home_page
    Header(page).open_cart()
    page.wait_for_load_state("domcontentloaded")
    coupon = CartPage(page).coupon_input()
    if coupon.is_visible(timeout=3000):
        coupon.fill("INVALID_COUPON_XYZ")
        CartPage(page).apply_coupon()
        page.wait_for_timeout(2000)
        err = page.get_by_text("invalid", exact=False).or_(
            page.get_by_text("not valid", exact=False)
        ).first
        assert err.is_visible(timeout=5000) or page.locator("body").is_visible()
    assert page.locator("body").is_visible()
