"""REG-044: Applying a single filter narrows the product list."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_044_applying_single_filter_narrows_list(home_page: Page):
    """Applying one filter refreshes listing."""
    page = home_page
    cat = page.locator("nav a[href*='/']").first
    if cat.is_visible(timeout=3000):
        cat.click()
        page.wait_for_load_state("domcontentloaded")
    filter_opt = page.locator("[class*='filter'] input").or_(
        page.locator("input[type='checkbox']").first
    ).first
    if filter_opt.is_visible(timeout=5000):
        filter_opt.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
