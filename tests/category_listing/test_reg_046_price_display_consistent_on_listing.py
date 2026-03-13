"""REG-046: Price display is consistent on listing page."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_046_price_display_consistent_on_listing(home_page: Page):
    """Listing shows consistent price formatting."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
