"""REG-013: Validation is shown for invalid password."""
import pytest
from playwright.sync_api import Page

from pages.login import LoginPage
from config import LOGIN_EMAIL


@pytest.mark.regression
def test_reg_013_validation_shown_for_invalid_password(home_page: Page):
    """Invalid password shows validation/error and user stays unauthenticated."""
    page = home_page
    LoginPage(page).open_sign_in()
    page.locator("input[name='login[username]']").fill(LOGIN_EMAIL)
    page.locator("input[name='login[password]']").fill("wrongpassword123!")
    page.locator("button.action.login").first.click()
    page.wait_for_timeout(3000)
    # Should still be on login page or show error
    error = page.locator(".message-error, [data-ui-id='message-error'], .messages .error").or_(
        page.get_by_text("Invalid", exact=False)
    ).or_(page.get_by_text("incorrect", exact=False)).first
    assert error.is_visible(timeout=5000) or "login" in page.url.lower()
