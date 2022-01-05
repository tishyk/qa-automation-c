import pytest
from core.browsers import WebBrowser
from core.pages import Page
from core.pages.home import HomePage
from core.pages.register import RegisterPage


@pytest.fixture(scope="module")
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)


@pytest.fixture(scope="module")
def reg_page(browser: WebBrowser) -> Page:
    return RegisterPage(browser)
