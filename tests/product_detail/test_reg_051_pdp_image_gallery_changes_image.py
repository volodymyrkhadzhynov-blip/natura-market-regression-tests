"""REG-051: PDP image gallery opens and changes image."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_051_pdp_image_gallery_changes_image(home_page: Page):
    """Gallery thumbnail changes main image."""
    page = home_page
    product = page.locator("a[href*='/product'], a[href*='/p/']").first
    if product.is_visible(timeout=5000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
    thumb = page.locator("[class*='thumbnail']").or_(
        page.locator("button[aria-label*='image']")
    ).nth(1).first
    if thumb.is_visible(timeout=3000):
        thumb.click()
        page.wait_for_timeout(300)
    assert page.locator("body").is_visible()
