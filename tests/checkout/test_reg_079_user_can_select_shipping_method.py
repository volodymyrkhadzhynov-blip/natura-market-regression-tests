"""REG-079: User can select a shipping method."""
import pytest


@pytest.mark.regression
def test_reg_079_user_can_select_shipping_method():
    """User can select one shipping method."""
    pytest.skip("Requires shipping methods loaded")
