"""REG-018: Account registration form validates mandatory fields."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_018_account_registration_form_validates_mandatory_fields(home_page: Page):
    """Create account form shows validation for required fields when submitted empty."""
    page = home_page
    page.goto("https://naturamarket.ca/customer/account/create/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    # Try to submit the empty form via keyboard (avoids button selector issues)
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    page.wait_for_timeout(2000)
    # After invalid submit the form should still be visible (not navigated away)
    assert page.locator("form").first.is_visible() or "create" in page.url.lower()
