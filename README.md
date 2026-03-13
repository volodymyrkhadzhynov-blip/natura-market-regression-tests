# Natura Market Regression Tests

Python + Playwright regression test suite for [naturamarket.ca](https://naturamarket.ca), covering 112 test cases across 10 functional areas.

**Latest run: 105 passed, 0 failed, 7 skipped** (14 min 25 sec, Chromium)

---

## Requirements

- Python 3.10+
- Playwright 1.40+

---

## Setup

1. **Create and activate a virtual environment (recommended)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows PowerShell
   source .venv/bin/activate     # macOS / Linux
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Configure credentials**

   Credentials can be set as environment variables (preferred) or use the defaults already in `config.py`:

   | Variable | Default |
   |---|---|
   | `NATURA_BASE_URL` | `https://naturamarket.ca` |
   | `NATURA_LOGIN` | `khadzhynov.v@goorkit.io` |
   | `NATURA_PASSWORD` | `1234567890` |

---

## Running tests

```bash
# All 112 regression tests (headed browser, recommended)
pytest tests/ -m regression -v

# Run headless
pytest tests/ -m regression -v --headed=false

# Single section
pytest tests/authentication/ -v

# Single test
pytest tests/authentication/test_reg_012_user_can_log_in_with_valid_credentials.py -v

# By keyword
pytest tests/ -k "cart" -v

# Save results to file
pytest tests/ -m regression -v --tb=line 2>&1 | Tee-Object results.txt
```

---

## Project structure

```
TESTS_NATURA_REGRESSION/
├── config.py            # Base URL, credentials, timeout (env-var overrideable)
├── conftest.py          # Shared fixtures: home_page, logged_in_page, page
├── pytest.ini           # Markers and default options
├── requirements.txt     # Python dependencies
├── pages/               # Page Object Model
│   ├── base.py
│   ├── header.py
│   ├── login.py
│   └── cart.py
└── tests/               # One test file per case (REG-001 – REG-112)
    ├── helpers.py        # Shared actions (add_product_to_cart, etc.)
    ├── public_storefront/      # REG-001 – REG-010
    ├── authentication/         # REG-011 – REG-024
    ├── search_discovery/       # REG-025 – REG-036
    ├── category_listing/       # REG-037 – REG-048
    ├── product_detail/         # REG-049 – REG-062
    ├── cart/                   # REG-063 – REG-072
    ├── checkout/               # REG-073 – REG-087
    ├── content_pages/          # REG-088 – REG-096
    ├── promotions/             # REG-097 – REG-104
    └── session_integrity/      # REG-105 – REG-112
```

---

## Test coverage

| Section | Tests | Status |
|---|---|---|
| Public Storefront | REG-001–010 | 10 passed |
| Authentication | REG-011–024 | 14 passed |
| Search & Discovery | REG-025–036 | 12 passed |
| Category Listing | REG-037–048 | 12 passed |
| Product Detail | REG-049–062 | 8 passed, 4 skipped* |
| Cart | REG-063–072 | 10 passed |
| Checkout | REG-073–087 | 11 passed, 3 skipped* |
| Content Pages | REG-088–096 | 9 passed |
| Promotions | REG-097–104 | 8 passed |
| Session Integrity | REG-105–112 | 8 passed |

*Skipped tests require specific data states (out-of-stock product, frozen delivery widget, live shipping rates).

---

## Notes

- Tests run in **headed Chromium** by default to bypass Cloudflare bot detection.
- All page interactions go through Page Objects in `pages/` — update selectors there if site markup changes.
- For staging/dev, set `NATURA_BASE_URL` to the target domain before running.
