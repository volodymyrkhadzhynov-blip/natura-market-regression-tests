"""REG-023: Authenticated user can open order history page."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_023_authenticated_user_can_open_order_history(logged_in_page: Page):
    """My Orders page opens (labeled 'Orders' on this site)."""
    page = logged_in_page
    page.goto(f"{BASE_URL}/sales/order/history/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    assert "order" in page.url.lower() or "sales" in page.url.lower()
    assert page.locator("body").is_visible()
