"""REG-105: Logged-in session persists after page refresh."""
import pytest
from playwright.sync_api import Page

from pages.login import LoginPage


@pytest.mark.regression
def test_reg_105_logged_in_session_persists_after_refresh(logged_in_page: Page):
    """After refresh user remains logged in."""
    page = logged_in_page
    page.reload()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)
    # If still logged in, URL stays on account page (not redirected to login)
    assert "account" in page.url.lower() and "login" not in page.url.lower()
