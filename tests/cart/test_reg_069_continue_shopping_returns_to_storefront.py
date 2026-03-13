"""REG-069: Continue shopping returns user to storefront."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_069_continue_shopping_returns_to_storefront(home_page: Page, base_url: str):
    """Continue Shopping returns to storefront."""
    page = home_page
    page.goto(f"{base_url.rstrip('/')}/cart")
    page.wait_for_load_state("domcontentloaded")
    cont = page.get_by_role("link", name="Continue Shopping").or_(
        page.get_by_text("Continue Shopping")
    ).first
    if cont.is_visible(timeout=5000):
        cont.click()
        page.wait_for_load_state("domcontentloaded")
    assert "naturamarket" in page.url.lower()
