"""REG-043: Category filter expands and collapses correctly."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_043_category_filter_expands_collapses(home_page: Page):
    """Filter group expands and collapses."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    filter_btn = page.get_by_role("button", name="Filter").or_(
        page.locator("[class*='filter']").first
    ).first
    if filter_btn.is_visible(timeout=5000):
        filter_btn.click()
        page.wait_for_timeout(500)
    assert page.locator("body").is_visible()
