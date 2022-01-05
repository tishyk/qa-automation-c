class RegistrationPage(object):
    """Represent registration page web element locators."""
    signup: str = '//a[@href="/signup"]'
    by_email: str = '//button[@value="email"]'
    by_phone: str = '//button[@value="phone"]'
    input_email: str = '//input[@type="email"]'
    input_phone: str = '//input[@type="tel"]'
    btn_continiue: str = '//button[contains(text(), "Continue")]'
    input_fullname: str = '//input[@type="text"]'
