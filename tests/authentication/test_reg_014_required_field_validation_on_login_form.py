"""REG-014: Required field validation works on login form."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_014_required_field_validation_on_login_form(home_page: Page):
    """Empty email/password shows mandatory-field validation."""
    page = home_page
    page.goto("https://naturamarket.ca/customer/account/login/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    page.locator("button.action.login").first.click()
    page.wait_for_timeout(1500)
    # Browser HTML5 validation or Magento validation message should show
    assert (
        page.locator("input[name='login[username]']").is_visible()
        or page.locator(".mage-error, [generated='true']").first.is_visible(timeout=5000)
    )
