import pytest
from pages.map.urls import HomePageUrl, RegisterPageUrl,  Url


@pytest.fixture(scope="module")
def home_url() -> Url:
    return HomePageUrl()

@pytest.fixture(scope="module")
def register_url() -> Url:
    return RegisterPageUrl()