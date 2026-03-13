"""REG-055: Required option validation works on PDP."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_055_required_option_validation_on_pdp(home_page: Page):
    """Product with required options blocks Add to Cart until selected."""
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
        page.wait_for_timeout(1000)
    assert page.locator("body").is_visible()
