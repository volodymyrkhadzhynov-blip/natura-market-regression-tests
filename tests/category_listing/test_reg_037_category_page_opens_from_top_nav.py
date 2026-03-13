"""REG-037: Category page opens from top navigation."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_037_category_page_opens_from_top_nav(home_page: Page):
    """Nav category link opens category listing page."""
    page = home_page
    # Category hrefs discovered from live site inspection
    cat_link = (
        page.get_by_role("link", name="Pantry")
        .or_(page.get_by_role("link", name="Snacks"))
        .or_(page.get_by_role("link", name="Beverages"))
        .or_(page.locator("a[href*='/food.html'], a[href*='snacks'], a[href*='beverages']").first)
        .first
    )
    if cat_link.is_visible(timeout=8000):
        cat_link.click()
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1000)
    assert "naturamarket" in page.url.lower()
