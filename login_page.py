from basepage import BasePage
from selenium.webdriver.common.by import By


class MainElements:

    signup = (By.XPATH, '//a[@href="/signup"]')
    by_email = (By.XPATH, '//button[@value="email"]')
    by_phone = (By.XPATH, '//button[@value="phone"]')
    input_email = (By.XPATH, '//input[@type="email"]')
    input_phone = (By.XPATH, '//input[@type="tel"]')
    btn_continiue = (By.XPATH, '//button[contains(text(), "Continue")]')
    input_fullname = (By.XPATH, '//input[@type="text"]')
    input_accid = (By.XPATH, '//input[@name="id"]')
    btn_create = (By.XPATH, '//button[contains(text(), "Create")]')
    btn_conn_gmail = (By.XPATH, '//button[@data-cloudsponge-source="gmail"]')
    btn_conn_icloud = (By.XPATH, '//button[@data-cloudsponge-source="icloud"]')
    btn_conn_office365 = (By.XPATH, '//button[@data-cloudsponge-source="office365"]')
    text_alert = (By.XPATH, '//div[@role="alert"]')
    create_nft = (By.XPATH, '//h5/../button')
    upload_window = (By.XPATH, '//div[@class="modal-dialog"]')
    input_files = (By.XPATH, '//input[@id="files"]')
    uploaded_img = (By.XPATH,'//img[@alt="Uploaded File"]')
    btn_next = (By.XPATH, '//button[contains(text(), "Next")]')
    input_title = (By.XPATH, '//input[@name="title"]')
    input_description = (By.XPATH, '//input[@name="description"]')
    input_size = (By.XPATH, '//input[@placeholder="Ex. Size"]')
    input_size_int = (By.XPATH, '//input[@placeholder="Ex. 40"]')
    select_category = (By.XPATH, '//select[@name="category"]')
    btn_mine = (By.XPATH, '//button[contains(text(), "Mine")]')
    btn_send = (By.XPATH, '//button[contains(text(), "Send")]')
