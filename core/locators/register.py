class RegistrationPage(object):
    """Represent registration page web element locators."""

    signup: str = '//a[@href="/signup"]'
    by_email: str = '//button[@value="email"]'
    by_phone: str = '//button[@value="phone"]'
    input_email: str = '//input[@type="email"]'
    input_phone: str = '//input[@type="tel"]'
    btn_continiue: str = '//button[contains(text(), "Continue")]'
    btn_login: str = '//button[contains(text(), "Login")]'
    input_fullname: str = '//input[@type="text"]'
    input_accid: str = '//input[@name="id"]'
    btn_create: str = '//button[contains(text(), "Create")]'
    btn_conn_gmail: str = '//button[@data-cloudsponge-source="gmail"]'
    btn_conn_icloud: str = '//button[@data-cloudsponge-source="icloud"]'
    btn_conn_office365: str = '//button[@data-cloudsponge-source="office365"]'
    window_for_create_nft: str = '//div[@role="dialog"]' #'//div[@class="modal-dialog"]'
    btn_next: str = '//button[contains(text(), "Next")]'

