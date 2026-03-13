"""REG-012: User can log in with valid credentials."""
import pytest
from playwright.sync_api import Page

from pages.login import LoginPage
from config import LOGIN_EMAIL, LOGIN_PASSWORD


@pytest.mark.regression
def test_reg_012_user_can_log_in_with_valid_credentials(home_page: Page):
    """Valid credentials log user in and redirect to account dashboard."""
    page = home_page
    LoginPage(page).login(LOGIN_EMAIL, LOGIN_PASSWORD)
    assert LoginPage(page).is_logged_in() or "account" in page.url.lower()
