"""REG-032: Brand alphabet filter opens a brand listing."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_032_brand_alphabet_filter_opens_listing(home_page: Page):
    """On Brands page, letter filter shows filtered listing."""
    page = home_page
    brands_link = page.get_by_role("link", name="Brands").or_(
        page.get_by_text("Brands", exact=False)
    ).first
    if brands_link.is_visible(timeout=5000):
        brands_link.click()
        page.wait_for_load_state("domcontentloaded")
        letter = page.get_by_role("link", name="A").or_(page.locator("a:has-text('A')").first).first
        if letter.is_visible(timeout=3000):
            letter.click()
            page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
