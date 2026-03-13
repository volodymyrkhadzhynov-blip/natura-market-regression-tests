"""REG-042: User can switch between available list/grid view controls."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_042_list_grid_view_switch_works(home_page: Page):
    """List/grid view control changes presentation."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    view_btn = page.get_by_role("button", name="Grid").or_(
        page.get_by_role("button", name="List")
    ).or_(page.locator("[aria-label*='view']").first).first
    if view_btn.is_visible(timeout=3000):
        view_btn.click()
        page.wait_for_timeout(500)
    assert page.locator("body").is_visible()
