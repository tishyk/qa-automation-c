from abc import ABC, abstractmethod
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.action_chains import ActionChains

class Element(ABC):
    """Abstraction of a web element."""

    @abstractmethod
    def text(self, by: str, value: str) -> str:
        pass

    @abstractmethod
    def element(self) -> webelement.WebElement:
        pass

    @abstractmethod
    def is_displayed(self) -> bool:
        pass

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def send_keys(self, value: str) -> None:
        pass

    @abstractmethod
    def click(self) -> None:
        pass


class WebElement(Element):
    """Represent concrete web element."""

    def __init__(self, element: webelement.WebElement) -> None:
        self._element = element

    def text(self, by: str, value: str) -> str:
        return self._element.find_element(by, value).text

    def element(self) -> webelement.WebElement:
        return self._element

    def is_displayed(self) -> bool:
        return self._element.is_displayed()

    def is_enabled(self) -> bool:
        return self._element.is_enabled()

    def clear(self) -> None:
        self._element.clear()

    def send_keys(self, value: str) -> None:
        self._element.send_keys(value)

    def click(self) -> None:
        self._element.click()

    def offset_click(self, x: int, y: int) -> None:
        action = ActionChains(self._element.parent)
        action.move_to_element_with_offset(self._element, x, y).click().perform()

