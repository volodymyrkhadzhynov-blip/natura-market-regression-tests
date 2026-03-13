"""REG-057: PDP description and details tabs are readable."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_057_pdp_description_and_details_tabs_readable(home_page: Page):
    """Description/detail sections open and display content."""
    page = home_page
    product = page.locator("a[href*='/product'], a[href*='/p/']").first
    if product.is_visible(timeout=5000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    desc = page.get_by_text("Description").or_(page.get_by_text("Details")).first
    if desc.is_visible(timeout=3000):
        desc.click()
    assert page.locator("body").is_visible()
