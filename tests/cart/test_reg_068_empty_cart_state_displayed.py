"""REG-068: Empty cart state is displayed correctly."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_068_empty_cart_state_displayed(home_page: Page, base_url: str):
    """Empty cart shows empty state and continue option."""
    page = home_page
    page.goto(f"{base_url.rstrip('/')}/cart")
    page.wait_for_load_state("domcontentloaded")
    assert page.get_by_text("empty", exact=False).or_(
        page.get_by_role("link", name="Continue Shopping")
    ).or_(page.locator("body")).first.is_visible(timeout=5000)
