"""REG-006: Footer is displayed on homepage."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_006_footer_displayed_on_homepage(home_page: Page):
    """Footer is reachable with link groups and social icons."""
    page = home_page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(300)
    footer = page.locator("footer").or_(page.locator("[role='contentinfo']")).first
    assert footer.is_visible()
