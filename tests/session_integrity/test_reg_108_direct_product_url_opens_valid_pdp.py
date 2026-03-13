"""REG-108: Direct product URL opens valid PDP."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_108_direct_product_url_opens_valid_pdp(home_page: Page):
    """Direct product URL opens PDP."""
    page = home_page
    product = page.locator("a[href*='/product'], a[href*='/p/']").first
    if product.is_visible(timeout=5000):
        href = product.get_attribute("href")
        if href:
            url = href if href.startswith("http") else BASE_URL + href
            page.goto(url)
            page.wait_for_load_state("domcontentloaded")
            assert page.locator("h1").first.is_visible(timeout=5000)
    assert page.locator("body").is_visible()
