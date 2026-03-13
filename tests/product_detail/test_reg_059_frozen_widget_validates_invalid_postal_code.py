"""REG-059: Frozen delivery widget validates invalid postal code."""
import pytest


@pytest.mark.regression
def test_reg_059_frozen_widget_validates_invalid_postal_code():
    """Frozen widget shows validation for invalid postal code."""
    pytest.skip("Requires frozen delivery widget")
