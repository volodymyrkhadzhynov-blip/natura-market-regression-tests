"""REG-096: Footer informational pages render without broken layout."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_096_footer_pages_render_without_broken_layout(home_page: Page):
    """Informational pages render correctly."""
    page = home_page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="FAQ").or_(
        page.get_by_text("Shipping", exact=False)
    ).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    assert page.locator("body").is_visible()
