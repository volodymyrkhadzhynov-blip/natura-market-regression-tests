"""Cart and mini cart."""
from playwright.sync_api import Page
from config import BASE_URL


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def view_cart_link(self):
        """'View cart' link in mini-cart panel (lowercase 'c' on site)."""
        return self.page.locator("a.action.secondary.checkout").or_(
            self.page.get_by_role("link", name="View cart")
        ).first

    def proceed_to_checkout(self):
        """Navigate to checkout — uses the Checkout link that has a real href."""
        # The full cart page has a.action.primary.checkout with href=/checkout?...
        # Mini-cart also has one but with empty href; target the one with real href.
        checkout_link = self.page.locator(
            "a.action.primary.checkout[href*='/checkout']"
        ).or_(
            self.page.locator("a[href*='/checkout?']")
        ).first
        if checkout_link.is_visible(timeout=5000):
            checkout_link.click()
        else:
            # Fallback: navigate directly to checkout
            self.page.goto(f"{BASE_URL}/checkout/", wait_until="domcontentloaded")
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(3000)

    def continue_shopping(self):
        self.page.get_by_role("link", name="Continue Shopping").or_(
            self.page.get_by_text("Continue Shopping")
        ).first.click()
        self.page.wait_for_load_state("domcontentloaded")

    def quantity_input(self, index: int = 0):
        return self.page.locator("input[name*='qty'], input[type='number']").nth(index)

    def remove_item(self, index: int = 0):
        # Use JavaScript to click delete button (avoids actionability/visibility issues)
        self.page.evaluate(f"""
            const btns = Array.from(document.querySelectorAll(
                'button.action-delete, .action-delete, a.action.delete, ' +
                'button[data-cart-item-delete], .cart.item button[type="button"]'
            ));
            if (btns[{index}]) btns[{index}].click();
        """)
        self.page.wait_for_timeout(1000)
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(2000)

    def coupon_input(self):
        return self.page.locator("input#coupon_code, input[name='coupon_code']").first

    def apply_coupon(self):
        self.page.locator("button.action.apply").or_(
            self.page.get_by_role("button", name="Apply")
        ).first.click()
        self.page.wait_for_timeout(2000)
