from tests.coverage.markers import unit
from core.map.urls import Url, base_url

home: str = "home"
about: str = "about-us"
contact: str = "contact-us"
signup: str = "signup"
sign_on: str = "sign_on"


@unit
def test_home_url(homepage_url: Url) -> None:
    assert homepage_url.get() == f"{base_url}/{home}"


@unit
def test_about_url(about_url: Url) -> None:
    assert about_url.get() == f"{base_url}/{about}"


@unit
def test_contact_url(contact_url: Url) -> None:
    assert contact_url.get() == f"{base_url}/{contact}"


@unit
def test_signup_url(register_url: Url) -> None:
    assert register_url.get() == f"{base_url}/{signup}"


@unit
def test_sign_on_url(sign_url: Url) -> None:
    assert sign_url.get() == f"{base_url}/{sign_on}"
