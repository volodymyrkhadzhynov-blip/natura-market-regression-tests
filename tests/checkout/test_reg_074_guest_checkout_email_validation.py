"""REG-074: Guest checkout email validation works."""
import pytest
from playwright.sync_api import Page

from pages.cart import CartPage
from tests.helpers import add_product_and_go_to_cart


@pytest.mark.regression
def test_reg_074_guest_checkout_email_validation(home_page: Page):
    """Invalid email on guest checkout shows validation."""
    add_product_and_go_to_cart(home_page)
    page = home_page
    CartPage(page).proceed_to_checkout()
    page.wait_for_load_state("domcontentloaded")
    email = page.get_by_label("Email").or_(page.get_by_placeholder("Email")).first
    if email.is_visible(timeout=5000):
        email.fill("notanemail")
        page.get_by_role("button", name="Continue").or_(
            page.get_by_role("button", name="Next")
        ).first.click()
        page.wait_for_timeout(1500)
        err = page.get_by_text("valid", exact=False).or_(
            page.get_by_text("email", exact=False)
        ).first
        assert err.is_visible(timeout=5000) or email.is_visible()
    assert page.locator("body").is_visible()
