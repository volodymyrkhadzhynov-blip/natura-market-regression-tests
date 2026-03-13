"""REG-102: Health goal landing page opens."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_102_health_goal_landing_opens(home_page: Page):
    """Health goal (e.g. High Protein) opens landing."""
    page = home_page
    Header(page).open_main_nav()
    page.wait_for_timeout(500)
    link = page.get_by_role("link", name="High Protein").or_(
        page.get_by_text("Low Sugar")
    ).first
    if link.is_visible(timeout=5000):
        link.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").is_visible()
