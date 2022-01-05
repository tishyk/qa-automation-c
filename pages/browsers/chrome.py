from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.browsers import WebBrowser
from pages.driver.web_driver import WebDriverOf
from pages.driver.driver import Driver
import os

class Chrome(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        service = Service(os.path.join(here, 'chromedriver.exe'))
        options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome()
        self._chrome: WebDriver = webdriver.Chrome(service=service, options=options)

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return "Chrome"
