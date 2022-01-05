import pytest
from core.map.urls import *


@pytest.fixture(scope="module")
def homepage_url() -> Url:
    return HomePageUrl()


@pytest.fixture(scope="module")
def register_url() -> Url:
    return RegisterPageUrl()


@pytest.fixture(scope="module")
def sign_url() -> Url:
    return SignOnPageUrl()


@pytest.fixture(scope="module")
def about_url() -> Url:
    return AboutUsPageUrl()


@pytest.fixture(scope="module")
def contact_url() -> Url:
    return ContactPageUrl()
