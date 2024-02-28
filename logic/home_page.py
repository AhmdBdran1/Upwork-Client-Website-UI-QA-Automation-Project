from time import sleep, time
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    LOGIN_BUTTON_XPATH = "//*[@id='nav-main']/div/a[1]"
    JOBS_NAV_XPATH = "//*[@id='nav-right']/ul/li[1]/button"
    POST_JOB_OPTION = "//*[@id='nav-right']/ul/li[1]/ul/li[1]/a"
    PROFILE_LOGO_XPATH ="//*[@id='nav-right']/ul/li[10]/button/div/span[2]"
    SETTINGS_BTN_XPATH = "//*[@id='nav-right']/ul/li[10]/ul/li[4]/ul/li[2]/a"
    NAME_OF_ACCOUNT_OWNER_XPATH = "//*[@id='nav-right']/ul/li[10]/ul/li[1]/div/div[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_XPATH))
        )

    def click_to_start_login(self):
        self.login_button.click()

    def click_on_profile_logo(self):
        profile_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_LOGO_XPATH))
        )
        profile_logo.click()

    def click_on_setting_btn(self):
        setting_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SETTINGS_BTN_XPATH))
        )
        setting_btn.click()

    def navigate_to_setting_page(self):
        self.click_on_profile_logo()
        self.click_on_setting_btn()


    def post_job_button(self):
        try:
            jobs_nav = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.JOBS_NAV_XPATH))
            )
            jobs_nav.click()
            post_job_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.POST_JOB_OPTION))
            )
            post_job_option.click()
            return True
        except Exception as e:
            print(e)
            return False

    def get_the_name_of_the_account_owner(self):
        self.click_on_profile_logo()
        name_of_owner = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NAME_OF_ACCOUNT_OWNER_XPATH))
        )
        return name_of_owner.text
