"""REG-036: Recipe or blog discovery link opens content page."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_036_recipe_or_blog_link_opens_content_page(home_page: Page):
    """Recipe or Blog from footer opens content page."""
    page = home_page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)
    blog = page.get_by_role("link", name="Blog").or_(
        page.get_by_role("link", name="Recipe")
    ).first
    if blog.is_visible(timeout=5000):
        blog.click()
        page.wait_for_load_state("domcontentloaded")
    assert page.url and "naturamarket" in page.url.lower()
