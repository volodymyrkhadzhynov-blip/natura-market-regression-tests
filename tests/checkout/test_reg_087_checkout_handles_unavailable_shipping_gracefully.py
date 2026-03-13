"""REG-087: Checkout handles unavailable shipping combination gracefully."""
import pytest


@pytest.mark.regression
def test_reg_087_checkout_handles_unavailable_shipping_gracefully():
    """Unserviceable address shows clear message."""
    pytest.skip("Requires specific unsupported address")
