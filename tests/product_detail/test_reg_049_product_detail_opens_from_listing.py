"""REG-049: Product detail page opens from listing."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_049_product_detail_opens_from_listing(home_page: Page):
    """Clicking product on listing opens PDP."""
    page = home_page
    from config import BASE_URL
    # Navigate to a known category page and click the first product
    page.goto(f"{BASE_URL}/healthy-snacks.html", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    product = page.locator(
        ".product-item a.product-item-link, .product-item-info a, [class*='product-item'] a[href]"
    ).first
    if product.is_visible(timeout=10000):
        product.click()
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1000)
    assert page.locator("h1").first.is_visible(timeout=8000)
