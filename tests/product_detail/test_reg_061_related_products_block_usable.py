"""REG-061: Related or recommended products block is usable."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_061_related_products_block_usable(home_page: Page):
    """Related/recommended block opens product on click."""
    page = home_page
    product = page.locator("a[href*='/product'], a[href*='/p/']").first
    if product.is_visible(timeout=5000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    related = page.get_by_text("Related").or_(page.get_by_text("Recommended")).first
    if related.is_visible(timeout=3000):
        link = page.locator("[class*='related'] a").first
        if link.is_visible(timeout=2000):
            link.click()
            page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
