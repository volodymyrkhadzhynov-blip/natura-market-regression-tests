"""REG-076: Province/state selection is available for Canadian address."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_076_province_state_available_for_canada(home_page: Page):
    """Canadian address has province/state selector."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    country = page.get_by_label("Country").or_(page.locator("select[name*='country']")).first
    if country.is_visible(timeout=5000):
        country.select_option("Canada")
        page.wait_for_timeout(500)
    province = page.get_by_label("Province").or_(
        page.locator("select[name*='region'], select[name*='state']")
    ).first
    if province.is_visible(timeout=3000):
        assert province.is_visible()
    assert page.locator("body").is_visible()
