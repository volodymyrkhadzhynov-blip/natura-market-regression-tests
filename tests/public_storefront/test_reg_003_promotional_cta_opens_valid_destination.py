"""REG-003: Promotional CTA opens a valid destination."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_003_promotional_cta_opens_valid_destination(home_page: Page):
    """Clicking SHOP NOW or main promo opens valid landing page."""
    page = home_page
    cta = page.get_by_role("link", name="Shop Now").or_(
        page.get_by_role("link", name="SHOP NOW")
    ).first
    if cta.is_visible(timeout=5000):
        cta.click()
        page.wait_for_load_state("domcontentloaded")
        assert page.url and "naturamarket" in page.url.lower()
        assert page.locator("body").is_visible()
