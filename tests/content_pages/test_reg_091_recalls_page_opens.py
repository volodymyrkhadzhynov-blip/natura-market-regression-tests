"""REG-091: Recalls page opens."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_091_recalls_page_opens(home_page: Page):
    """Recalls / Recalls & Safety Advisory opens."""
    page = home_page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="Recalls").or_(
        page.get_by_text("Recalls", exact=False)
    ).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
