from time import sleep, time
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    JOBS_NAV_XPATH = "//button[contains(@aria-labelledby,'caret-btn-jobPosting')]"
    POST_JOB_OPTION = "//a[normalize-space()='Post a Job']"
    PROFILE_LOGO_XPATH = "//span[@class='up-s-nav-icon nav-avatar nav-user-avatar']"
    SETTINGS_BTN_XPATH = "//a[normalize-space()='Settings']"
    NAME_OF_ACCOUNT_OWNER_XPATH = ("//div[@class='nav-d-flex align-items-center']//"
                                   "div[@class='nav-user-label'][normalize-space()='Ahmd Bdran']")
    INPUT_SEARCH_XPATH = "//form[@id='navSearchForm-desktop']//input[@placeholder='Search']"
    SEARCH_DROP_DOWN = "//ul[@id='autocomplete-dropdown']"

    def __init__(self, driver):
        super().__init__(driver)
        self.jobs_nav = None
        self.profile_logo = None
        self.driver = driver
        self.profile_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_LOGO_XPATH))
        )
        self.jobs_nav = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.JOBS_NAV_XPATH))
        )

    def click_on_profile_logo(self):

        self.profile_logo.click()

    def click_on_setting_btn(self):
        setting_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SETTINGS_BTN_XPATH))
        )
        setting_btn.click()

    def click_on_search_input_and_insert_text(self):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_SEARCH_XPATH))
        )
        search_input.click()
        search_input.send_keys("flu")

    def navigate_to_setting_page(self):
        self.click_on_profile_logo()
        self.click_on_setting_btn()

    def post_job_button(self):
        try:

            self.jobs_nav.click()
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

    def check_dropdown_exist(self):
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SEARCH_DROP_DOWN))
            )
            return True
        except Exception as e:
            print(e)
            return False



