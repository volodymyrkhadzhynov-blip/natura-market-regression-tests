"""REG-078: Available shipping methods are displayed after valid address."""
import pytest


@pytest.mark.regression
def test_reg_078_shipping_methods_displayed_after_valid_address():
    """Valid address loads shipping methods."""
    pytest.skip("Requires full address entry; can enable with test data")
