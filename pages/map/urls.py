from abc import ABC, abstractmethod


base_url = "https://dev.nftmakerapp.io/"


class Url(ABC):
    """Abstraction of a page url."""

    @abstractmethod
    def get(self) -> str:
        pass


class PageUrl(Url):
    """Represent web page url."""

    def __init__(self, url: str) -> None:
        self._url: str = url

    def get(self) -> str:
        return self._url


class HomePageUrl(Url):
    """Represent home page url."""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{base_url}/home")

    def get(self) -> str:
        return self._url.get()


class RegisterPageUrl(Url):
    """Represent home page url."""

    def __init__(self) -> None:
        self._url: Url = PageUrl(f"{base_url}/signup")

    def get(self) -> str:
        return self._url.get()