"""REG-021: Authenticated user can open account information page."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_021_authenticated_user_can_open_account_information(logged_in_page: Page):
    """Account Information page opens and shows profile fields."""
    page = logged_in_page
    page.goto(f"{BASE_URL}/customer/account/edit/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    assert "account" in page.url.lower() or "edit" in page.url.lower()
    assert page.locator("input[name='firstname'], input[name='email']").first.is_visible(timeout=5000)
