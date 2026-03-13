"""REG-060: Frozen delivery widget accepts valid postal code."""
import pytest


@pytest.mark.regression
def test_reg_060_frozen_widget_accepts_valid_postal_code():
    """Frozen widget accepts valid postal code."""
    pytest.skip("Requires frozen delivery widget")
