from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from core.browsers import WebBrowser
from core.driver.web_driver import WebDriverOf
from core.driver.driver import Driver
import core
import os


class Chrome(WebBrowser):
    """Representation of a chrome web browser"""

    def __init__(self) -> None:
        here = os.path.dirname(core.__path__[0])
        service = Service(os.path.join(here, 'chromedriver.exe'))
        options = webdriver.ChromeOptions()
        self._chrome: WebDriver = webdriver.Chrome(service=service, options=options)

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return "Chrome"
