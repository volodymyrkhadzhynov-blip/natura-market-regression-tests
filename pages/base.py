"""Base page and common helpers."""
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def goto(self, path: str = "", wait_until: str = "domcontentloaded"):
        url = f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url
        self.page.goto(url, wait_until=wait_until)

    def get_link(self, text: str, exact: bool = False):
        if exact:
            return self.page.get_by_role("link", name=text)
        return self.page.get_by_role("link", name=text)

    def wait_for_page_load(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle", timeout=10000)
