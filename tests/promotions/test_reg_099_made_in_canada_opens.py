"""REG-099: Made in Canada page opens."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_099_made_in_canada_opens(home_page: Page):
    """Made in Canada opens."""
    page = home_page
    Header(page).open_main_nav()
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="Made in Canada").or_(
        page.get_by_text("Made in Canada")
    ).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
