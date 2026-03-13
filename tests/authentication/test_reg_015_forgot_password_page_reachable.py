"""REG-015: Forgot Password page is reachable."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_015_forgot_password_page_reachable(home_page: Page):
    """Forgot Password link opens reset page with email entry."""
    page = home_page
    page.goto("https://naturamarket.ca/customer/account/login/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    forgot = page.locator("a[href*='forgotpassword']").or_(
        page.get_by_role("link", name="Forgot Your Password?")
    ).first
    if forgot.is_visible(timeout=5000):
        forgot.click()
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1000)
    assert "forgot" in page.url.lower() or "reset" in page.url.lower() or page.locator("input[name='email']").is_visible()
