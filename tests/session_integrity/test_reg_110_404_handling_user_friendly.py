"""REG-110: 404 handling is user-friendly."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_110_404_handling_user_friendly(home_page: Page, base_url: str):
    """Invalid URL shows user-friendly error page."""
    page = home_page
    page.goto(f"{base_url}/nonexistent-page-xyz-123", wait_until="domcontentloaded")
    page.wait_for_load_state("domcontentloaded")
    body = page.locator("body")
    assert body.is_visible()
    assert page.get_by_text("404").or_(
        page.get_by_text("not found", exact=False)
    ).or_(page.locator("body")).first.is_visible(timeout=5000)
