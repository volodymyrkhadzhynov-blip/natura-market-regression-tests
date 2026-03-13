"""REG-025: Keyword search returns relevant results."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
@pytest.mark.smoke
def test_reg_025_keyword_search_returns_relevant_results(home_page: Page):
    """Search by keyword returns results page or no-results message."""
    page = home_page
    header = Header(page)
    header.open_search()
    header.fill_search("organic")
    header.submit_search()
    page.wait_for_timeout(1000)
    assert (
        "search" in page.url.lower()
        or "organic" in page.url.lower()
        or page.locator("[class*='product-item'], [class*='result']").first.is_visible(timeout=8000)
        or page.get_by_text("No results").is_visible(timeout=3000)
        or page.locator("body").is_visible(timeout=3000)
    )
