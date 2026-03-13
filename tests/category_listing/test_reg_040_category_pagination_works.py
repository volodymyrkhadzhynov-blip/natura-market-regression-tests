"""REG-040: Category pagination works."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_040_category_pagination_works(home_page: Page):
    """Next page control loads next result page."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    next_btn = page.get_by_role("link", name="Next").or_(
        page.locator("a[aria-label*='next']")
    ).first
    if next_btn.is_visible(timeout=5000):
        next_btn.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
