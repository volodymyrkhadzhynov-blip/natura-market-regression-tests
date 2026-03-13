"""REG-017: Create account page is reachable."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_017_create_account_page_reachable(home_page: Page):
    """Create an Account opens registration page."""
    page = home_page
    page.goto("https://naturamarket.ca/customer/account/create/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    assert "create" in page.url.lower() or "register" in page.url.lower()
    assert page.locator("input[name='firstname']").or_(
        page.locator("input[name='email']")
    ).first.is_visible(timeout=5000)
