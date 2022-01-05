from tests.coverage.markers import smoke
from pages.pages.register import RegisterPage


@smoke
def test_register_page_register_text(register_page: RegisterPage) -> None:
    assert register_page.register_text().is_displayed()



