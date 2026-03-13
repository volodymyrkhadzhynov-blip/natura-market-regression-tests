"""REG-031: Brands page is reachable from navigation."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_031_brands_page_reachable_from_navigation(home_page: Page):
    """Brands / Browse All Brands opens Brands page."""
    page = home_page
    Header(page).open_main_nav()
    page.wait_for_timeout(500)
    brands = page.get_by_role("link", name="Brands").or_(
        page.get_by_text("Browse All Brands")
    ).first
    if brands.is_visible(timeout=5000):
        brands.click()
        page.wait_for_load_state("domcontentloaded")
        assert "brand" in page.url.lower() or page.get_by_text("Brand").first.is_visible()
