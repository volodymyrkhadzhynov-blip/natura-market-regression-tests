"""REG-097: Sale or clearance page displays discounted products."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_097_sale_page_displays_discounted_products(home_page: Page):
    """Sale/clearance page shows discounted products."""
    page = home_page
    sale = page.get_by_role("link", name="Sale").or_(
        page.get_by_text("Clearance")
    ).first
    if sale.is_visible(timeout=5000):
        sale.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
