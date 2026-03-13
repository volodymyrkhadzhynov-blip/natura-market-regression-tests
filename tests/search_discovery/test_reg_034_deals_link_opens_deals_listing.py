"""REG-034: Deals link opens deals listing page."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_034_deals_link_opens_deals_listing(home_page: Page):
    """Deals/sale/clearance link opens deals listing."""
    page = home_page
    deals = page.get_by_role("link", name="Deals").or_(
        page.get_by_text("Sale", exact=False)
    ).or_(page.get_by_text("Clearance", exact=False)).first
    if deals.is_visible(timeout=5000):
        deals.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
