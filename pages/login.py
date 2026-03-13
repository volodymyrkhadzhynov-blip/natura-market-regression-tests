"""Login and account pages."""
from playwright.sync_api import Page
from config import BASE_URL


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open_sign_in(self):
        """Navigate directly to the sign-in page (more reliable than clicking link)."""
        self.page.goto(f"{BASE_URL}/customer/account/login/", wait_until="domcontentloaded")
        self.page.wait_for_timeout(2000)

    def fill_email(self, email: str):
        self.page.locator("input[name='login[username]']").fill(email)

    def fill_password(self, password: str):
        self.page.locator("input[name='login[password]']").fill(password)

    def click_sign_in(self):
        self.page.locator("button.action.login").first.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(2000)

    def login(self, email: str, password: str):
        self.open_sign_in()
        self.fill_email(email)
        self.fill_password(password)
        self.click_sign_in()

    def get_forgot_password_link(self):
        return self.page.locator("a[href*='forgotpassword']").first

    def get_create_account_link(self):
        return self.page.locator("a[href*='customer/account/create']").first

    def is_logged_in(self) -> bool:
        """Check that Log Out link is visible (indicates logged in)."""
        return self.page.locator("a[href*='customer/account/logout']").first.is_visible(timeout=5000)
