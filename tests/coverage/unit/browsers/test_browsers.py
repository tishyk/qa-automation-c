import pytest
from tests.coverage.markers import unit
from core.browsers import WebBrowserError


@unit
def test_browser_error() -> None:
    with pytest.raises(WebBrowserError):
        raise WebBrowserError("Raised WebBrowserError!")
