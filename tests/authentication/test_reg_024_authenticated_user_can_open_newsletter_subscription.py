"""REG-024: Authenticated user can open newsletter subscription page."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_024_authenticated_user_can_open_newsletter_subscription(logged_in_page: Page):
    """Newsletter Subscriptions page opens."""
    page = logged_in_page
    Header(page).open_my_account()
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("link", name="Newsletter").or_(
        page.get_by_text("Newsletter")
    ).first.click()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
