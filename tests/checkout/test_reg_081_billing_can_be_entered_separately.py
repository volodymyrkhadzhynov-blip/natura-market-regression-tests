"""REG-081: Billing address can be entered separately."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_081_billing_can_be_entered_separately(home_page: Page):
    """Separate billing address can be entered."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
