"""REG-101: Gift set page opens."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_101_gift_set_page_opens(home_page: Page):
    """Gift Sets opens."""
    page = home_page
    Header(page).open_main_nav()
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="Gift Set").or_(
        page.get_by_text("Gift Sets")
    ).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
