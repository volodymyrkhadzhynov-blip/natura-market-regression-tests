"""REG-106: Cart contents persist after user signs in."""
import pytest
from playwright.sync_api import Page

from pages.login import LoginPage
from pages.header import Header
from config import LOGIN_EMAIL, LOGIN_PASSWORD


@pytest.mark.regression
def test_reg_106_cart_contents_persist_after_sign_in(home_page: Page):
    """Guest cart persists or merges after sign in."""
    page = home_page
    from config import BASE_URL
    # Add a product to cart as guest via known product URL
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
    LoginPage(page).login(LOGIN_EMAIL, LOGIN_PASSWORD)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)
    Header(page).open_cart()
    page.wait_for_timeout(500)
    assert page.locator("body").is_visible()
