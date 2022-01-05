import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    here = os.path.dirname(os.path.abspath(__file__))
    service = Service(os.path.join(here, 'chromedriver.exe'))
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()