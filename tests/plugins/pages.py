import pytest
from pages.browsers import WebBrowser
from pages.pages import Page
from pages.pages.home import HomePage
from pages.pages.register import RegisterPage


@pytest.fixture(scope="module")
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)


@pytest.fixture(scope="module")
def register_page(browser: WebBrowser) -> Page:
    return RegisterPage(browser)
