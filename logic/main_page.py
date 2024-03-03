from time import sleep, time
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    LOGIN_BUTTON_XPATH = "//*[@id='nav-main']/div/a[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_XPATH))
        )

    def click_to_start_login(self):
        self.login_button.click()






