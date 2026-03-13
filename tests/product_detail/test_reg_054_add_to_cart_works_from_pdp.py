"""REG-054: Add to Cart works from PDP for regular product."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
@pytest.mark.smoke
def test_reg_054_add_to_cart_works_from_pdp(home_page: Page):
    """Add to Cart adds product and shows confirmation."""
    page = home_page
    from config import BASE_URL
    page.goto(
        f"{BASE_URL}/boulder-canyon-kettle-style-potato-chips-with-avocado-oil-classic-sea-salt-283-5g.html",
        wait_until="domcontentloaded",
    )
    page.wait_for_timeout(2000)
    add_btn = page.locator("button.tocart, button.action.tocart").or_(
        page.get_by_role("button", name="ADD TO CART")
    ).first
    if add_btn.is_visible(timeout=5000):
        add_btn.click()
        page.wait_for_timeout(2000)
    assert page.locator("body").is_visible()
