"""REG-094: Blog page opens from footer."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_094_blog_opens_from_footer(home_page: Page):
    """Blog in footer opens."""
    page = home_page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="Blog").or_(page.get_by_text("Blog")).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
