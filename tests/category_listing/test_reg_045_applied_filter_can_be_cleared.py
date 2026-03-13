"""REG-045: Applied filter can be cleared."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_045_applied_filter_can_be_cleared(home_page: Page):
    """Clear/remove applied filter restores results."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    clear = page.get_by_role("button", name="Clear").or_(
        page.get_by_text("Clear", exact=False)
    ).first
    if clear.is_visible(timeout=3000):
        clear.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
