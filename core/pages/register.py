from selenium.webdriver.support.select import Select
from core.browsers import WebBrowser
from core.map.conditions import ExpectedCondition
from core.driver.driver import Driver
from core.map.elements import Element
from core.map.handlers import HandlerBy, WebHandlerBy
from core.input.register import RegisterPageInput
from core.locators.register import RegistrationPage as RP_Locators
from core.pages.base import BasePage
from core.map.urls import RegisterPageUrl, Url
from core.map.waits import WebDriverWaitOf


def set_input_value(element, input_: RegisterPageInput) -> None:
    element.clear()
    element.send_keys(input_)


class RegisterPage(BasePage):
    """Represent register page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._rp_locators: RP_Locators = RP_Locators()
        self._page = BasePage(browser, RegisterPageUrl())
        self.input_ = RegisterPageInput

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def by_xpath(self, locator):
        return self.driver().find_element(self._by.xpath(), locator)

    def by_xp_arr(self, locator):
        return self.driver().find_elements(self._by.xpath(), locator)[-1]

    def signup(self) -> Element:
        return self.by_xpath(self._rp_locators.signup)

    def register_by_email(self) -> Element:
        return self.by_xpath(self._rp_locators.by_email)

    def register_by_phone(self) -> Element:
        return self.by_xpath(self._rp_locators.by_phone)

    def input_account_id(self) -> Element:
        return self.by_xpath(self._rp_locators.input_accid)

    def input_email(self) -> Element:
        return self.by_xpath(self._rp_locators.input_email)

    def input_fullname(self) -> Element:
        return self.by_xpath(self._rp_locators.input_fullname)

    def input_phone(self) -> Element:
        return self.by_xpath(self._rp_locators.input_phone)

    def button_continiue(self) -> Element:
        return self.by_xpath(self._rp_locators.btn_continiue)

    def button_create(self) -> Element:
        return self.by_xpath(self._rp_locators.btn_create)

    def button_login(self) -> Element:
        return self.by_xpath(self._rp_locators.btn_login)

    def set_email(self) -> None:
        set_input_value(self.input_email(), self.input_.email)

    def set_fullname(self) -> None:
        set_input_value(self.input_fullname(), self.input_.full_name)

    def set_account_id(self) -> None:
        set_input_value(self.input_account_id(), self.input_.accid)

    def button_connect_gmail(self) -> Element:
        return self.by_xp_arr(self._rp_locators.btn_conn_gmail)

    def button_connect_icloud(self) -> Element:
        return self.by_xpath(self._rp_locators.btn_conn_icloud)

    def button_connect_office365(self) -> Element:
        return self.by_xpath(self._rp_locators.btn_conn_office365)

    def window_for_create_nft(self):
        return self.by_xpath(self._rp_locators.window_for_create_nft)
