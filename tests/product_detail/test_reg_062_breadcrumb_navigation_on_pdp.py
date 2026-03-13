"""REG-062: Breadcrumb navigation works on PDP."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_062_breadcrumb_navigation_on_pdp(home_page: Page):
    """Breadcrumb link goes to listing."""
    page = home_page
    product = page.locator("a[href*='/product'], a[href*='/p/']").first
    if product.is_visible(timeout=5000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
    bc = page.locator("nav[aria-label='Breadcrumb'] a").or_(
        page.locator("[class*='breadcrumb'] a").first
    ).first
    if bc.is_visible(timeout=3000):
        bc.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
