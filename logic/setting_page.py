from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingPage(BasePage):
    PASSWORD_AND_SECURITY_BTN_XPATH = "//*[@id='main']/div[2]/div[4]/div[1]/div/nav/div/div/ul/li[3]/a/span"
    EDIT_PASSWORD_BTN_XPATH = "//*[@id='button-password']"
    INPUT_OLD_PASSWORD_XPATH = "//*[@id='changePassword_oldPassword']"
    INPUT_NEW_PASSWORD_XPATH = "//*[@id='changePassword_password']"
    INPUT_CONFIRM_NEW_PASSWORD_XPATH = "//*[@id='changePassword_confirmPassword']"
    SAVE_CHANGES_BTN = "//*[@id='control_save']"
    CONFIRM_PASSWORD_MESSAGE_XPATH = "//*[@id='confirmPassword-message']/span"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_password_and_security_btn(self):
        password_and_security_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PASSWORD_AND_SECURITY_BTN_XPATH))
        )
        password_and_security_btn.click()

    def click_on_edit_password_icon(self):
        edit_password_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.EDIT_PASSWORD_BTN_XPATH))
        )
        edit_password_btn.click()

    def insert_old_password(self):
        input_old_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_OLD_PASSWORD_XPATH))
        )
        input_old_password.send_keys("Ahm2023bdr")

    def insert_new_password(self):
        input_new_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_NEW_PASSWORD_XPATH))
        )
        input_new_password.send_keys("Ah2024bdr")

    def insert_confirm_new_password(self):
        input_confirm_new_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_CONFIRM_NEW_PASSWORD_XPATH))
        )
        input_confirm_new_password.send_keys("Ah2024bddr")

    def save_password_changes(self):
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SAVE_CHANGES_BTN))
        )
        save_btn.click()

    def get_confirm_password_message(self):
        message_text_view = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CONFIRM_PASSWORD_MESSAGE_XPATH))
        )
        return message_text_view.text

    def change_current_password(self):
        self.click_on_password_and_security_btn()
        self.click_on_edit_password_icon()
        self.insert_old_password()
        self.insert_new_password()
        self.insert_confirm_new_password()
        self.save_password_changes()
