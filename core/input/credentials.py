import json
import os
import core


def read_cred():
    here = os.path.dirname(core.__path__[0])
    filename = os.path.join(here, "secret.json")
    with open(filename) as f:
        return json.load(f)


class Credential(object):
    """Represent sign on page input data."""
    all_cred = read_cred()
    google_cred = all_cred.get("google")
    amazon_cred = all_cred.get("amazon")
    os.environ["AWS_ACCESS_KEY"] = AWS_ACCESS_KEY = amazon_cred.get("access_kid")
    os.environ["AWS_SECRET_KEY"] = AWS_SECRET_KEY = amazon_cred.get("secret_acc_key")
    arn: str = amazon_cred.get("arn")
    g_user_name: str = google_cred.get("login")
    g_password: str = google_cred.get("password")
