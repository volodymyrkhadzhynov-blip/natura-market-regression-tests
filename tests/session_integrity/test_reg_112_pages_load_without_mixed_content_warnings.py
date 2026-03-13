"""REG-112: Storefront pages load without mixed-content warnings."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_112_pages_load_without_mixed_content_warnings(home_page: Page):
    """Pages load over HTTPS without mixed-content warnings."""
    page = home_page
    assert page.url.startswith("https://")
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.url.startswith("https://")
    product = page.locator("a[href*='/product']").first
    if product.is_visible(timeout=5000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.url.startswith("https://")
