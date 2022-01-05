from tests.coverage.markers import smoke
from core.pages.register import RegisterPage
# import time


@smoke
def test_reg_page_by_email(register_page: RegisterPage) -> None:
    assert register_page.register_by_email().is_displayed()


@smoke
def test_reg_page_by_phone(register_page: RegisterPage) -> None:
    assert register_page.register_by_phone().is_displayed()


@smoke
def test_reg_page_input_email(register_page: RegisterPage) -> None:
    register_page.register_by_email().click()
    assert register_page.input_email().is_displayed()


@smoke
def test_reg_page_input_phone(register_page: RegisterPage) -> None:
    register_page.register_by_phone().click()
    assert register_page.input_phone().is_displayed()


@smoke
def test_reg_page_button_continiue(register_page: RegisterPage) -> None:
    assert register_page.button_continiue().is_displayed()
    assert register_page.button_continiue().is_enabled() is False, "Button must be disabled"


@smoke
def test_reg_page_button_login(register_page: RegisterPage) -> None:
    assert register_page.button_login().is_displayed()
    assert register_page.button_login().is_enabled(), "Button must be enabled"


@smoke
def test_register_by_email(register_page: RegisterPage) -> None:
    #TODO: Add a TC with mobile registration
    register_page.register_by_email().click()
    register_page.set_email()
    register_page.button_continiue().click()
    assert register_page.input_fullname().is_displayed()
    assert register_page.input_account_id().is_displayed()
    assert register_page.button_create().is_displayed()
    register_page.set_fullname()
    register_page.set_account_id()
    assert register_page.button_create().is_enabled()
    register_page.button_create().click()
    assert register_page.button_connect_gmail().is_enabled()
    assert register_page.button_connect_icloud().is_enabled()
    assert register_page.button_connect_office365().is_enabled()
    #TODO: As it turned out, to implement a click past the window to import contacts is not easy,
    # so this TC is not implemented yet
    register_page.button_connect_gmail().aclick()



