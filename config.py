"""Configuration for Natura Market regression tests."""
import os

BASE_URL = os.getenv("NATURA_BASE_URL", "https://naturamarket.ca")
LOGIN_EMAIL = os.getenv("NATURA_LOGIN", "khadzhynov.v@goorkit.io")
LOGIN_PASSWORD = os.getenv("NATURA_PASSWORD", "1234567890")
DEFAULT_TIMEOUT_MS = 30000
