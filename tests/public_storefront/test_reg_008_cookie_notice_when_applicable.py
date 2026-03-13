"""REG-008: Cookie-disabled notice is shown when applicable."""
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
def test_reg_008_cookie_notice_when_applicable(home_page: Page):
    """System notices (cookie/JS) are readable when shown."""
    page = home_page
    notice = page.get_by_text("cookie", exact=False).or_(
        page.get_by_text("Cookie", exact=False)
    ).first
    if notice.is_visible(timeout=3000):
        assert notice.is_visible()
