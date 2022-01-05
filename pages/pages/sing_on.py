from pages.browsers import WebBrowser
from pages.map.conditions import ExpectedCondition
from pages.driver.driver import Driver
from pages.map.elements import Element
from pages.map.handlers import HandlerBy, WebHandlerBy
from pages.input.sign_on import SignOnPageInput
from pages.locators.sing_on import SingOnPage as SP_Locators
from pages.pages import Page
from pages.pages.base import BasePage
from pages.map.urls import SignOnPageUrl, Url
from pages.map.waits import WebDriverWaitOf


class SignOnPage(Page):
    """Represent sign-on page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._sp_locators: SP_Locators = SP_Locators()
        self._page: Page = BasePage(browser, SignOnPageUrl())

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def user_name(self, input_: SignOnPageInput) -> None:
        field: Element = self.driver().find_element(self._by.xpath(), self._sp_locators.user_name)
        field.clear()
        field.send_keys(input_.user_name)

    def password(self, input_: SignOnPageInput) -> None:
        field: Element = self.driver().find_element(self._by.xpath(), self._sp_locators.password)
        field.clear()
        field.send_keys(input_.password)

    def text(self) -> Element:
        return WebDriverWaitOf(self.driver()).until_presence_of_element_located(
            ExpectedCondition(self._by.xpath(), self._sp_locators.txt)
        )

    def register_link(self) -> Element:
        return WebDriverWaitOf(self.driver()).until_presence_of_element_located(
            ExpectedCondition(self._by.xpath(), self._sp_locators.register_link)
        )

    def login(self) -> None:
        self.driver().find_element(self._by.xpath(), self._sp_locators.login).click()
