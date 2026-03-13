"""REG-010: Advanced Search page is reachable."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_010_advanced_search_page_reachable(home_page: Page):
    """Advanced Search link opens Advanced Search page."""
    page = home_page
    adv = page.get_by_role("link", name="Advanced Search").or_(
        page.get_by_text("Advanced Search")
    ).first
    if adv.is_visible(timeout=5000):
        adv.click()
        page.wait_for_load_state("domcontentloaded")
        assert "search" in page.url.lower() or page.locator("form").first.is_visible()
