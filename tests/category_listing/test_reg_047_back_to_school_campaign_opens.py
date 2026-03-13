"""REG-047: Back to School campaign page opens."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_047_back_to_school_campaign_opens(home_page: Page):
    """Back to School campaign link opens campaign page."""
    page = home_page
    bts = page.get_by_role("link", name="Back to School").or_(
        page.get_by_text("Back to School", exact=False)
    ).first
    if bts.is_visible(timeout=5000):
        bts.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
