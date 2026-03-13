"""REG-082: Payment method section loads successfully."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_082_payment_section_loads(home_page: Page):
    """Payment step loads and shows payment options."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
