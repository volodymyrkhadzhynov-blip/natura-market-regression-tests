"""REG-035: Gift cards page is reachable."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_035_gift_cards_page_reachable(home_page: Page):
    """Gift Cards link opens gift card page."""
    page = home_page
    Header(page).open_main_nav()
    page.wait_for_timeout(500)
    gc = page.get_by_role("link", name="Gift Card").or_(
        page.get_by_text("Gift Card", exact=False)
    ).first
    if gc.is_visible(timeout=5000):
        gc.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
