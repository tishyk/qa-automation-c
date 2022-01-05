from selenium.webdriver import Remote
from selenium.webdriver.chrome.webdriver import WebDriver
from core.browsers import WebBrowser
from core.driver.web_driver import WebDriverOf
from core.driver.driver import Driver
from core.input.credentials import Credential as cred
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import boto3

class RemoteBrowser(WebBrowser):
    """Representation of a remote web browser."""


    def __init__(self, remote_url: str = "localhost:9515") -> None:
        client = boto3.client(
            "devicefarm",
            region_name='us-west-2',
            aws_access_key_id=cred.AWS_ACCESS_KEY,
            aws_secret_access_key=cred.AWS_SECRET_KEY,
        )
        testgrid_url_response = client.create_test_grid_url(
            projectArn=cred.arn,
            expiresInSeconds=300
        )
        desired_caps = webdriver.ChromeOptions()
        desired_caps.add_argument("--start-maximized")
        self._remote: WebDriver = Remote(
            command_executor=testgrid_url_response['url'], options=desired_caps
        )

    def driver(self) -> Driver:
        return WebDriverOf(self._remote)

    def name(self) -> str:
        return "Remote"
