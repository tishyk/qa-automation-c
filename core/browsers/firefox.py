from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from core.browsers import WebBrowser
from core.driver.web_driver import WebDriverOf
from core.driver.driver import Driver


class FireFox(WebBrowser):
    """Representation of a firefox web browser."""

    def __init__(self) -> None:
        self._firefox: WebDriver = webdriver.Firefox()

    def driver(self) -> Driver:
        return WebDriverOf(self._firefox)

    def name(self) -> str:
        return "Firefox"
