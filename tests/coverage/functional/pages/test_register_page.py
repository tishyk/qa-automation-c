from tests.coverage.markers import smoke
from core.pages.register import RegisterPage
import time


@smoke
def test_reg_page_by_email(reg_page: RegisterPage) -> None:
    assert reg_page.register_by_email().is_displayed()


@smoke
def test_reg_page_by_phone(reg_page: RegisterPage) -> None:
    assert reg_page.register_by_phone().is_displayed()


@smoke
def test_reg_page_input_email(reg_page: RegisterPage) -> None:
    reg_page.register_by_email().click()
    assert reg_page.input_email().is_displayed()


@smoke
def test_reg_page_input_phone(reg_page: RegisterPage) -> None:
    reg_page.register_by_phone().click()
    assert reg_page.input_phone().is_displayed()


@smoke
def test_reg_page_button_continiue(reg_page: RegisterPage) -> None:
    assert reg_page.button_continiue().is_displayed()
    assert reg_page.button_continiue().is_enabled() is False, "Button must be disabled"


@smoke
def test_reg_page_button_login(reg_page: RegisterPage) -> None:
    assert reg_page.button_login().is_displayed()
    assert reg_page.button_login().is_enabled(), "Button must be enabled"


@smoke
def test_register_by_email(reg_page: RegisterPage) -> None:
    #TODO: Add a TC with mobile registration
    reg_page.register_by_email().click()
    reg_page.set_email()
    reg_page.button_continiue().click()
    assert reg_page.input_fullname().is_displayed()
    assert reg_page.input_account_id().is_displayed()
    assert reg_page.button_create().is_displayed()
    reg_page.set_fullname()
    reg_page.set_account_id()
    assert reg_page.button_create().is_enabled()
    reg_page.button_create().click()
    assert reg_page.button_connect_gmail().is_enabled()
    assert reg_page.button_connect_icloud().is_enabled()
    assert reg_page.button_connect_office365().is_enabled()
    #TODO: As it turned out, to implement import from google is not easy,
    # so this TC is not implemented yet
    reg_page.window_for_create_nft().offset_click(-100, -100)
    assert reg_page.button_next().is_displayed()
    #reg_page.window_google_login(reg_page.button_connect_gmail())



