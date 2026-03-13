"""REG-111: Multiple tabs keep consistent session state."""
import pytest
from playwright.sync_api import Page

from pages.login import LoginPage


@pytest.mark.regression
def test_reg_111_multiple_tabs_consistent_session(logged_in_page: Page, base_url: str):
    """New tab keeps authenticated state."""
    page = logged_in_page
    context = page.context
    new_page = context.new_page()
    new_page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    # Navigate to account page in new tab — if logged in, no redirect to login
    new_page.goto(f"{base_url}/customer/account/", wait_until="domcontentloaded")
    new_page.wait_for_timeout(2000)
    assert "account" in new_page.url.lower() and "login" not in new_page.url.lower()
    new_page.close()
