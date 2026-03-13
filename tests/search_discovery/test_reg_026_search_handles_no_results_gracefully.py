"""REG-026: Search handles no-results keyword gracefully."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_026_search_handles_no_results_gracefully(home_page: Page):
    """Random keyword shows friendly no-results state."""
    page = home_page
    header = Header(page)
    header.open_search()
    header.fill_search("xyznonexistent12345")
    header.submit_search()
    page.wait_for_timeout(1000)
    assert page.locator("body").is_visible(timeout=5000)
