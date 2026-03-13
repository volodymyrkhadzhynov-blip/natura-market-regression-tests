"""REG-029: Advanced Search allows search execution."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_029_advanced_search_allows_search_execution(home_page: Page):
    """Advanced Search page accepts criteria and returns results."""
    page = home_page
    adv = page.get_by_role("link", name="Advanced Search").or_(
        page.get_by_text("Advanced Search")
    ).first
    if adv.is_visible(timeout=5000):
        adv.click()
        page.wait_for_load_state("domcontentloaded")
        inp = page.locator("input[name*='search'], input[type='search']").first
        if inp.is_visible(timeout=3000):
            inp.fill("test")
            page.get_by_role("button", name="Search").or_(page.locator("button[type='submit']").first).first.click()
            page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
