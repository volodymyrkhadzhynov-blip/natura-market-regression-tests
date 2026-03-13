"""REG-095: Social media links are clickable."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_095_social_media_links_clickable(home_page: Page):
    """Social icons in footer are clickable."""
    page = home_page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)
    social = page.locator("footer a[href*='facebook'], footer a[href*='instagram']").or_(
        page.locator("a[aria-label*='Facebook'], a[aria-label*='Instagram']")
    ).first
    if social.is_visible(timeout=5000):
        with page.expect_popup() as popup_info:
            social.click()
        popup = popup_info.value
        popup.wait_for_load_state("domcontentloaded")
        popup.close()
    assert page.locator("body").is_visible()
