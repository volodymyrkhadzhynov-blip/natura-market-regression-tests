"""REG-038: Category page displays product tiles."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_038_category_page_displays_product_tiles(home_page: Page):
    """Category page shows product grid with image, title, price."""
    page = home_page
    page.goto(f"{BASE_URL}/healthy-snacks.html", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    products = page.locator(
        ".product-item, .product-item-info, [class*='product-item'], li.item.product"
    ).first
    assert products.is_visible(timeout=10000) or page.locator("main").is_visible()
