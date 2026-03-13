"""REG-019: Authenticated user can open My Account dashboard."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_019_authenticated_user_can_open_my_account_dashboard(logged_in_page: Page):
    """Logged-in user can open My Account dashboard."""
    page = logged_in_page
    Header(page).open_my_account()
    page.wait_for_load_state("domcontentloaded")
    assert "account" in page.url.lower() or page.get_by_text("Account").first.is_visible()
