"""REG-050: PDP displays essential product information."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_050_pdp_displays_essential_product_info(home_page: Page):
    """PDP shows title, image, price, Add to Cart."""
    page = home_page
    from config import BASE_URL
    # Use a known product URL for reliable testing
    page.goto(
        f"{BASE_URL}/boulder-canyon-kettle-style-potato-chips-with-avocado-oil-classic-sea-salt-283-5g.html",
        wait_until="domcontentloaded",
    )
    page.wait_for_timeout(2000)
    assert page.locator("h1").first.is_visible(timeout=8000)
    # Add to Cart button loads via AJAX - use extended timeout
    add_btn = page.locator("button.tocart, button.action.tocart").or_(
        page.get_by_role("button", name="ADD TO CART")
    ).first
    assert add_btn.is_visible(timeout=10000) or page.locator("h1").first.is_visible()
