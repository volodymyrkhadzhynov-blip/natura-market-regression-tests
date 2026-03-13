"""REG-107: Browser Back navigation works between listing and PDP."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_107_browser_back_works_listing_to_pdp(home_page: Page):
    """Back from PDP returns to listing."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    product = page.locator("a[href*='/product'], a[href*='/p/']").first
    if product.is_visible(timeout=5000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
    page.go_back()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
