"""REG-020: Authenticated user can log out."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_020_authenticated_user_can_log_out(logged_in_page: Page):
    """Log Out closes session and returns to guest state."""
    page = logged_in_page
    Header(page).sign_out()
    # After logout the 'Sign in' link should appear
    assert page.locator("a[href*='customer/account/login']").or_(
        page.get_by_role("link", name="Sign in")
    ).first.is_visible(timeout=10000)
