import pytest
from core.browsers.chrome import WebBrowser, Chrome
from core.browsers.remote import RemoteBrowser

local = False#True
if local:
    @pytest.fixture(scope="session")
    def browser() -> WebBrowser:
        browser: WebBrowser = Chrome()
        yield browser
        browser.driver().close()
else:
    @pytest.fixture(scope="session")
    def browser() -> WebBrowser:
        browser: WebBrowser = RemoteBrowser()
        yield browser
        browser.driver().close()
