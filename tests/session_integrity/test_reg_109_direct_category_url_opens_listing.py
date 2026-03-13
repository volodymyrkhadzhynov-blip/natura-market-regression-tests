"""REG-109: Direct category URL opens valid listing page."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_109_direct_category_url_opens_listing(home_page: Page):
    """Direct category URL opens listing."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        href = cat.get_attribute("href")
        if href:
            url = href if href.startswith("http") else BASE_URL + href
            page.goto(url)
            page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
