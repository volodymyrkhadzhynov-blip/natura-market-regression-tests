"""REG-022: Authenticated user can open address book page."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_022_authenticated_user_can_open_address_book(logged_in_page: Page):
    """Address Book page opens."""
    page = logged_in_page
    page.goto(f"{BASE_URL}/customer/address/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    assert "address" in page.url.lower()
    assert page.locator("body").is_visible()
