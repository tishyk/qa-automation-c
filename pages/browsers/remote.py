from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.browsers import WebBrowser
from pages.driver.web_driver import WebDriverOf
from pages.driver.driver import Driver


class RemoteBrowser(WebBrowser):
    """Representation of a remote web browser."""

    def __init__(self, remote_url: str = "localhost:9515") -> None:
        self._remote: WebDriver = Remote(
            command_executor=remote_url, desired_capabilities=ChromeOptions().to_capabilities()
        )

    def driver(self) -> Driver:
        return WebDriverOf(self._remote)

    def name(self) -> str:
        return "Remote"
