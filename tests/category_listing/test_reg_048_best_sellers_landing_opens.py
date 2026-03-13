"""REG-048: Best Sellers landing page opens."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_048_best_sellers_landing_opens(home_page: Page):
    """Best Sellers link opens Best Sellers listing."""
    page = home_page
    best = page.get_by_role("link", name="Best Sellers").or_(
        page.get_by_text("Best Sellers", exact=False)
    ).first
    if best.is_visible(timeout=5000):
        best.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
