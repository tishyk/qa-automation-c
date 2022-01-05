class HomePage(object):
    """Represent home page web element locators."""

    signup: str = '//a[@href="/signup"]'
    about: str = '//a[@href="/about-us"]'
    contact: str = '//a[@href="/contact-us"]'
    login: str = '//button[contains(text(), "Login")]'

