"""REG-056: Out-of-stock product state is displayed correctly."""
import pytest


@pytest.mark.regression
def test_reg_056_out_of_stock_displayed_correctly():
    """Out-of-stock product shows status and prevents invalid purchase."""
    pytest.skip("Requires known out-of-stock product URL")
