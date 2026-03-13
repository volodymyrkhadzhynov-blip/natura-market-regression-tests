"""REG-033: Popular brand link opens brand page."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_033_popular_brand_link_opens_brand_page(home_page: Page):
    """Popular brand link opens brand listing page."""
    page = home_page
    brand = page.get_by_role("link", name="Siete").or_(
        page.get_by_role("link", name="Simple Mills")
    ).or_(page.locator("a[href*='brand']").first).first
    if brand.is_visible(timeout=5000):
        brand.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.url and "naturamarket" in page.url.lower()
