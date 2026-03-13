"""Shared helpers for regression tests."""
from playwright.sync_api import Page
from config import BASE_URL


def add_product_to_cart(page: Page) -> None:
    """Navigate to a known product and add it to cart."""
    # Use a stable product URL to ensure consistent behavior
    page.goto(
        f"{BASE_URL}/boulder-canyon-kettle-style-potato-chips-with-avocado-oil-classic-sea-salt-283-5g.html",
        wait_until="domcontentloaded",
    )
    page.wait_for_timeout(2000)
    add_btn = page.locator("button.tocart").or_(
        page.get_by_role("button", name="ADD TO CART")
    ).or_(page.locator("button.action.tocart").first).first
    if add_btn.is_visible(timeout=5000):
        add_btn.click()
        page.wait_for_timeout(2000)


def add_product_and_go_to_cart(page: Page) -> None:
    """Add product and navigate to full cart page."""
    add_product_to_cart(page)
    page.goto(f"{BASE_URL}/checkout/cart/", wait_until="domcontentloaded")
    page.wait_for_timeout(1000)
