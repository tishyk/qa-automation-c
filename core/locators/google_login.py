class GoogleLogin(object):
    """Represent google login page web element locators."""

    email: str = '//*[@id="Email"]'
    btn_next: str = '//*[@id="next"]'
    password: str = '//*[@id="Passwd"]'
    signin: str = '//*[@id="signIn"]'
