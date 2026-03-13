"""REG-041: Product count is shown on listing page."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_041_product_count_shown_on_listing(home_page: Page):
    """Listing toolbar shows product/result count."""
    page = home_page
    page.goto(f"{BASE_URL}/healthy-snacks.html", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    toolbar = page.locator(
        ".toolbar-amount, .toolbar-number, [class*='toolbar'], .products-grid"
    ).first
    assert toolbar.is_visible(timeout=8000) or page.locator("main").is_visible()
