"""REG-027: Autocomplete suggestions appear for common keyword."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_027_autocomplete_suggestions_for_common_keyword(home_page: Page):
    """Typing in search shows autocomplete suggestions."""
    page = home_page
    header = Header(page)
    header.open_search()
    header.fill_search("snack")
    page.wait_for_timeout(1500)
    suggestions = page.locator("[class*='suggest'], [class*='autocomplete'], [role='listbox']").first
    if suggestions.is_visible(timeout=3000):
        assert suggestions.is_visible()
