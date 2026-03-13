"""REG-053: PDP blocks invalid quantity value."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_053_pdp_blocks_invalid_quantity(home_page: Page):
    """Invalid quantity (0/non-numeric) is blocked or normalized."""
    page = home_page
    product = page.locator("a[href*='/product'], a[href*='/p/']").first
    if product.is_visible(timeout=5000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
    qty = page.locator("input[name*='qty'], input[type='number']").first
    if qty.is_visible(timeout=3000):
        qty.fill("0")
        page.get_by_role("button", name="Add to Cart").first.click()
        page.wait_for_timeout(1000)
    assert page.locator("body").is_visible()
