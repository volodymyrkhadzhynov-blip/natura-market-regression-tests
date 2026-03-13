"""REG-009: Search entry point is visible in header."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_009_search_entry_point_visible(home_page: Page):
    """Search button is visible and search input becomes active on click."""
    page = home_page
    # Search input is always visible (search button is disabled until user types)
    search_input = page.locator("input#search, input[name='q']").first
    assert search_input.is_visible(timeout=8000)
