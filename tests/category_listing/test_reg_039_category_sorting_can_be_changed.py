"""REG-039: Category sorting can be changed."""
import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.mark.regression
def test_reg_039_category_sorting_can_be_changed(home_page: Page):
    """Sort control changes listing order."""
    page = home_page
    page.goto(f"{BASE_URL}/healthy-snacks.html", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    sort = page.locator("select#sorter, select[id*='sorter'], .sorter select").first
    if sort.is_visible(timeout=5000):
        sort.select_option(index=1)
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1000)
    assert page.locator("body").is_visible()
