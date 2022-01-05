import pytest
from core.browsers.chrome import WebBrowser, Chrome


@pytest.fixture(scope="session")
def browser() -> WebBrowser:
    browser: WebBrowser = Chrome()
    yield browser
    browser.driver().close()
