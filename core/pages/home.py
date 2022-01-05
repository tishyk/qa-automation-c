from core.browsers import WebBrowser
from core.driver.driver import Driver
from core.map.elements import Element
from core.map.handlers import HandlerBy, WebHandlerBy
from core.locators.home import HomePage as HP_Locators
from core.pages.base import BasePage
from core.map.urls import HomePageUrl, Url


class HomePage(BasePage):
    """Represent home page"""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._hp_locators: HP_Locators = HP_Locators()
        self._page = BasePage(browser, HomePageUrl())

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def by_xpath(self, locator):
        return self.driver().find_element(self._by.xpath(), locator)

    def signup(self) -> Element:
        return self.by_xpath(self._hp_locators.signup)

    def about(self) -> Element:
        return self.by_xpath(self._hp_locators.about)

    def contact(self) -> Element:
        return self.by_xpath(self._hp_locators.contact)

    def login(self) -> Element:
        return self.by_xpath(self._hp_locators.login)
