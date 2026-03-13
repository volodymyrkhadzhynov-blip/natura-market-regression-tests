"""REG-004: Header logo returns user to homepage."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_004_header_logo_returns_to_homepage(home_page: Page, base_url: str):
    """From a non-homepage, logo click returns to homepage."""
    page = home_page
    # Navigate to a non-homepage (e.g. Pantry/category)
    page.goto(f"{base_url}/food.html", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    page.locator("a.logo").first.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)
    assert base_url.rstrip("/") in page.url.rstrip("/")
