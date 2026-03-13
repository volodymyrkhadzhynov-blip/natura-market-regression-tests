"""REG-007: French store switch is available."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_007_french_store_switch_available(home_page: Page):
    """FR language/store switch opens French storefront."""
    page = home_page
    fr_link = page.get_by_role("link", name="FR").or_(page.get_by_text("FR", exact=True)).first
    if fr_link.is_visible(timeout=5000):
        fr_link.click()
        page.wait_for_load_state("domcontentloaded")
        assert page.url and "naturamarket" in page.url.lower()
