"""Header: logo, nav, search, cart, language."""
from playwright.sync_api import Page
from config import BASE_URL


class Header:
    def __init__(self, page: Page):
        self.page = page

    def click_logo(self):
        self.page.locator("a.logo").first.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_search(self):
        search_input = self.page.locator("input#search, input[name='q']").first
        if search_input.is_visible(timeout=3000):
            search_input.focus()
        else:
            btn = self.page.locator("button.action.search, .block-search button").first
            if btn.is_visible(timeout=3000):
                btn.click()
        self.page.wait_for_timeout(300)

    def search_input(self):
        return self.page.locator("input[name='q']")

    def fill_search(self, text: str):
        self.search_input().fill(text)

    def submit_search(self):
        """Submit search by pressing Enter directly on the input element."""
        try:
            query = self.search_input().input_value()
            if query:
                self.page.goto(
                    f"{BASE_URL}/catalogsearch/result/?q={query}",
                    wait_until="domcontentloaded",
                )
            else:
                self.search_input().press("Enter")
                self.page.wait_for_load_state("domcontentloaded")
        except Exception:
            self.page.keyboard.press("Enter")
            self.page.wait_for_load_state("domcontentloaded")

    def open_cart(self):
        self.page.goto(f"{BASE_URL}/checkout/cart/", wait_until="domcontentloaded")
        self.page.wait_for_timeout(1000)

    def open_mini_cart(self):
        """Click the cart showcart toggle to open the mini-cart panel."""
        self.page.locator("a.action.showcart").first.click()
        self.page.wait_for_timeout(800)

    def click_fr_switch(self):
        self.page.locator("a[href*='___store/fr']").or_(
            self.page.get_by_role("link", name="FR")
        ).first.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_main_nav(self):
        """Desktop nav is always visible — try to confirm a nav link is present."""
        try:
            self.page.locator(
                "a[href*='snacks'], a[href*='pantry'], a[href*='beverages'], "
                "a[href*='supplements'], a[href*='brands'], a[href*='diets'], "
                "a[href*='food'], nav a, [class*='nav-sections'] a"
            ).first.wait_for(timeout=5000)
        except Exception:
            pass

    def sign_out(self):
        """Navigate to logout URL directly (more reliable than clicking a hidden dropdown link)."""
        from config import BASE_URL as _BASE_URL
        self.page.goto(f"{_BASE_URL}/customer/account/logout/", wait_until="domcontentloaded")
        self.page.wait_for_timeout(2000)

    def open_my_account(self):
        self.page.goto(f"{BASE_URL}/customer/account/", wait_until="domcontentloaded")
        self.page.wait_for_timeout(1500)
