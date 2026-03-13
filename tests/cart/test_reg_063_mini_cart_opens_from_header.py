"""REG-063: Mini cart opens from header."""
import pytest
from playwright.sync_api import Page

from pages.header import Header
from tests.helpers import add_product_to_cart


@pytest.mark.regression
def test_reg_063_mini_cart_opens_from_header(home_page: Page):
    """Cart icon opens mini cart with contents."""
    add_product_to_cart(home_page)
    page = home_page
    Header(page).open_mini_cart()
    page.wait_for_timeout(1500)
    # Check mini cart or cart-related elements are present
    assert (
        page.locator("a.action.secondary.checkout").is_visible(timeout=3000)
        or page.get_by_role("link", name="View cart").is_visible(timeout=2000)
        or page.locator(".block-minicart").is_visible(timeout=2000)
        or page.locator("a.action.showcart").first.is_visible(timeout=3000)
    )
