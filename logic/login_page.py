from time import sleep, time
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    INPUT_EMAIL_XPATH = "//*[@id='login_username']"
    CONTINUE_WITH_EMAIL_BTN_XPATH = "//*[@id='login_password_continue']"
    INPUT_PASSWORD_XPATH = "//*[@id='login_password']"
    LOGIN_BUTTON_AFTER_INSERT_DATA_XPATH = "//*[@id='login_control_continue']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        try:
            input_email = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.INPUT_EMAIL_XPATH))
            )
            input_email.send_keys("ahmd1997bdran@gmail.com")

            continue_with_email_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.CONTINUE_WITH_EMAIL_BTN_XPATH))
            )
            continue_with_email_button.click()

            input_password = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.INPUT_PASSWORD_XPATH))
            )
            input_password.send_keys("Ahm2023bdr")

            login_button_after_insert_data = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_AFTER_INSERT_DATA_XPATH))
            )
            login_button_after_insert_data.click()
            sleep(10)
            return True
        except Exception as e:
            print("An error occurred:", e)
            return False

    def login_with_wrong_credential(self):
        try:
            input_email = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.INPUT_EMAIL_XPATH))
            )
            input_email.send_keys("ahmd1997bdran@gmail.com")

            continue_with_email_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.CONTINUE_WITH_EMAIL_BTN_XPATH))
            )
            continue_with_email_button.click()

            input_password = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.INPUT_PASSWORD_XPATH))
            )
            input_password.send_keys("wrong password")

            login_button_after_insert_data = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_AFTER_INSERT_DATA_XPATH))
            )
            login_button_after_insert_data.click()
            return True
        except Exception as e:
            print("An error occurred:", e)
            return False

