import random

def get_random_string():
    return random.choice(["u", "v", "w", "x", "y", "z"])+random.choice(["s", "o", "p", "t", "h", "i"]).join([
        random.choice(["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]),
        random.choice(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"]),
        ])

class RegisterPageInput(object):
    """Represent register page input data."""

    first_name: str = get_random_string()
    last_name: str = get_random_string()
    full_name: str = " ".join([first_name, last_name])
    phone: str = "+709-319-789"
    accid: str = get_random_string()
    email: str = accid+"@1secmail.com"
    country: str = "USA"
    password: str = get_random_string()
