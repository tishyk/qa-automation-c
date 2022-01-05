from abc import ABC, abstractmethod


base_url = "https://dev.nftmakerapp.io"


class Url(ABC):
    """Abstraction of a page url."""

    @abstractmethod
    def get(self) -> str:
        pass


class PageUrl(Url):
    """Represent common web page url"""

    def __init__(self, url: str) -> None:
        self._url: str = url

    def get(self) -> str:
        return self._url


class HomePageUrl(Url):
    """Represent home page url"""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{base_url}/home")

    def get(self) -> str:
        return self._url.get()


class RegisterPageUrl(Url):
    """Represent register page url"""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{base_url}/signup")

    def get(self) -> str:
        return self._url.get()


class SignOnPageUrl(Url):
    """Represent register page url"""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{base_url}/sign_on")

    def get(self) -> str:
        return self._url.get()


class AboutUsPageUrl(Url):
    """Represent about us url"""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{base_url}/about-us")

    def get(self) -> str:
        return self._url.get()


class ContactPageUrl(Url):
    """Represent contact url"""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{base_url}/contact-us")

    def get(self) -> str:
        return self._url.get()