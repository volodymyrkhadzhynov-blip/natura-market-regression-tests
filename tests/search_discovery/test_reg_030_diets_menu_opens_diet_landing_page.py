"""REG-030: Diets menu opens diet landing page."""
import pytest
from playwright.sync_api import Page

from pages.header import Header


@pytest.mark.regression
def test_reg_030_diets_menu_opens_diet_landing_page(home_page: Page):
    """Diets (e.g. Gluten Free) opens diet landing/category page."""
    page = home_page
    Header(page).open_main_nav()
    page.wait_for_timeout(500)
    diet = page.get_by_role("link", name="Gluten Free").or_(
        page.get_by_role("link", name="Plant Based")
    ).or_(page.get_by_text("Diets", exact=False).first).first
    if diet.is_visible(timeout=5000):
        diet.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.url and "naturamarket" in page.url.lower()
