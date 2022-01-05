from tests.coverage.markers import smoke
from core.pages.home import HomePage


@smoke
def test_home_signup_is_displayed(home_page: HomePage) -> None:
    """Check signup button"""
    assert home_page.signup().is_displayed()
    assert home_page.signup().is_enabled(), "Button must be enabled"


@smoke
def test_home_login_is_displayed(home_page: HomePage) -> None:
    """Check login button"""
    assert home_page.login().is_displayed()
    assert home_page.login().is_enabled(), "Button must be enabled"


def test_home_about_is_displayed(home_page: HomePage) -> None:
    """Check About in menu"""
    assert home_page.about().is_displayed()


def test_home_contact_is_displayed(home_page: HomePage) -> None:
    """Check Contact in menu"""
    assert home_page.contact().is_displayed()
