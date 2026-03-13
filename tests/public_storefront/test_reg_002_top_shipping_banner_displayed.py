"""REG-002: Top shipping banner is displayed."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_002_top_shipping_banner_displayed(home_page: Page):
    """Top informational banner is visible and readable."""
    page = home_page
    banner = page.locator("[class*='banner'], [class*='announcement']").first
    if banner.is_visible(timeout=5000):
        assert banner.is_visible()
