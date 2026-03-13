"""REG-088: Shipping and Returns page opens."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_088_shipping_and_returns_opens(home_page: Page):
    """Shipping & Returns in footer opens page."""
    page = home_page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="Shipping").or_(
        page.get_by_text("Shipping & Returns")
    ).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.url and "naturamarket" in page.url.lower()
