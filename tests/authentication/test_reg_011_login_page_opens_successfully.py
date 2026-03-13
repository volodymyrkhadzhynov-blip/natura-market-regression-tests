"""REG-011: Login page opens successfully."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_011_login_page_opens_successfully(home_page: Page):
    """Sign in page opens; email/password fields and sign-in action visible."""
    page = home_page
    page.locator("a[href*='customer/account/login']").first.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)
    assert "login" in page.url.lower() or "account" in page.url.lower()
    assert page.locator("input[name='login[username]']").is_visible()
    assert page.locator("input[name='login[password]']").is_visible()
    assert page.locator("button.action.login").is_visible()
