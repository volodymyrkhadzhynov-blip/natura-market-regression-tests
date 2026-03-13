"""REG-058: Frozen or refrigerated availability widget is displayed when applicable."""
import pytest


@pytest.mark.regression
def test_reg_058_frozen_availability_widget_when_applicable():
    """Frozen/refrigerated PDP shows delivery eligibility widget when applicable."""
    pytest.skip("Requires frozen/refrigerated product")
