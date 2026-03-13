"""Pytest and Playwright fixtures for Natura Market regression tests."""
import pytest
from playwright.sync_api import Page, BrowserContext

from config import BASE_URL, LOGIN_EMAIL, LOGIN_PASSWORD, DEFAULT_TIMEOUT_MS

STEALTH_JS = "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Launch headed Chrome with automation flags disabled to bypass Cloudflare."""
    return {
        **browser_type_launch_args,
        "headless": False,
        "args": [
            "--disable-blink-features=AutomationControlled",
            "--start-maximized",
        ],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Shared context args: viewport, locale, realistic user-agent."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "locale": "en-CA",
        "user_agent": UA,
    }


@pytest.fixture
def page(context: BrowserContext):
    """Override default page to inject stealth JS before each page load."""
    pg = context.new_page()
    pg.add_init_script(STEALTH_JS)
    pg.set_default_timeout(DEFAULT_TIMEOUT_MS)
    yield pg
    pg.close()


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def credentials():
    return {"email": LOGIN_EMAIL, "password": LOGIN_PASSWORD}


@pytest.fixture
def timeout_ms():
    return DEFAULT_TIMEOUT_MS


@pytest.fixture
def home_page(page: Page, base_url: str):
    """Open homepage and return page."""
    page.goto(base_url, wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    return page


@pytest.fixture
def logged_in_page(page: Page, base_url: str):
    """Log in with valid credentials and return page."""
    page.goto(
        f"{base_url}/customer/account/login/",
        wait_until="domcontentloaded",
    )
    page.wait_for_timeout(3000)
    page.locator("input[name='login[username]']").fill(LOGIN_EMAIL)
    page.locator("input[name='login[password]']").fill(LOGIN_PASSWORD)
    page.locator("button.action.login").or_(
        page.get_by_role("button", name="Sign In")
    ).first.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)
    return page
