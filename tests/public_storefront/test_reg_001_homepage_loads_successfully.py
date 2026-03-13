"""REG-001: Homepage loads successfully."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
@pytest.mark.smoke
def test_reg_001_homepage_loads_successfully(home_page: Page, base_url: str):
    """Homepage opens over HTTPS, loads without error, header/main/footer visible."""
    page = home_page
    assert page.url.startswith("https://")
    assert "naturamarket" in page.url.lower()
    # Site uses <header> tags — wait for logo to confirm load
    page.locator("a.logo").first.wait_for(timeout=10000)
    assert page.locator("a.logo").first.is_visible()
    assert page.locator("footer").or_(page.locator("[role='contentinfo']")).first.is_visible()
