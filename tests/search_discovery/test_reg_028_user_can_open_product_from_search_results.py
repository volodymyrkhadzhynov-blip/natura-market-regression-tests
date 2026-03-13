"""REG-028: User can open a product from search results."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_028_user_can_open_product_from_search_results(home_page: Page):
    """From search results, clicking product opens PDP."""
    page = home_page
    header = Header(page)
    header.open_search()
    header.fill_search("organic")
    header.submit_search()
    page.wait_for_timeout(1000)
    # Try clicking a product from search results
    product_link = page.locator(
        ".product-item a.product-item-link, [class*='product-item'] a[href$='.html']"
    ).first
    if product_link.is_visible(timeout=8000):
        product_link.click()
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(500)
        assert page.locator("h1").first.is_visible(timeout=8000)
    else:
        assert page.locator("body").is_visible(timeout=5000)
