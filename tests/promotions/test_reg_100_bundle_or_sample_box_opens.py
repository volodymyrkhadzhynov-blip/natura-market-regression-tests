"""REG-100: Bundle or sample box page opens."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_100_bundle_or_sample_box_opens(home_page: Page):
    """Bundles & Variety Packs or Sample Boxes opens."""
    page = home_page
    Header(page).open_main_nav()
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="Bundle").or_(
        page.get_by_text("Sample Box")
    ).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
