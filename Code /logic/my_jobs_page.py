from time import sleep, time
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyJobsPage(BasePage): # logic page for my jobs page
    POST_CARD_OPTIONS_BUTTON_XPATH = "//*[@id='dropdown-secondary-label-29']"
    REMOVE_POSTING_OPTION_XPATH = "//*[@id='popper_1']/div/div/div/div[1]/div/div/div/div/ul/li[7]"
    REASON_FOR_CLOSE_THE_JOB_XPATH = "//*[@id='reasons-dropdown']/div/div"
    ACCIDENTAL_JOB_POSTING_REASON_XPATH = "//*[@id='dropdown-menu']/li[1]/span"
    CLOSE_JOB_BUTTON_XPATH = "/html/body/div[8]/div/div[2]/div/div/div[3]/div/button[2]"
    EDIT_POSTING_OPTION_XPATH = "//*[@id='popper_1']/div/div/div/div[1]/div/div/div/div/ul/li[6]"
    EDIT_THE_TITLE_OF_THE_POST_XPATH = "//*[@id='main']/div[3]/div[4]/div[3]/header/div/div/button"
    INPUT_OF_THE_NEW_TITLE_XPATH = "//*[@id='title-1']"
    SAVE_BTN_XPATH = "/html/body/div[10]/div/div[2]/div/div/div[3]/div/button[2]"
    SAVE_JOB_POST_XPATH = "//*[@id='main']/div[3]/div[4]/div[2]/button"
    JOB_TITLE_XPATH = "//*[@id='air3-line-clamp-1']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_post_card_options_button(self):
        post_options_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.POST_CARD_OPTIONS_BUTTON_XPATH))
        )
        post_options_button.click()

    def select_remove_post_option(self):
        remove_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.REMOVE_POSTING_OPTION_XPATH))
        )
        remove_option.click()

    def select_edit_post_option(self):
        edit_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.EDIT_POSTING_OPTION_XPATH))
        )
        edit_option.click()

    def edit_post_title_option(self):
        title_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.EDIT_THE_TITLE_OF_THE_POST_XPATH))
        )
        title_option.click()

    def change_the_title_of_post(self):
        input_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_OF_THE_NEW_TITLE_XPATH))
        )
        input_title.clear()
        input_title.send_keys("new title")

    def click_on_save(self):
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_BTN_XPATH))
        )
        save_btn.click()

    def click_on_save_the_post(self):
        save_job_post_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_JOB_POST_XPATH))
        )
        save_job_post_btn.click()

    def dropdown_reasons_of_the_delete(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.REASON_FOR_CLOSE_THE_JOB_XPATH))
        )
        dropdown.click()

    def select_a_reason_for_remove(self):
        remove_reason = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ACCIDENTAL_JOB_POSTING_REASON_XPATH))
        )
        remove_reason.click()

    def click_on_close_job_button(self):
        close_job_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CLOSE_JOB_BUTTON_XPATH))
        )
        close_job_button.click()

    def get_job_title(self):
        job_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.JOB_TITLE_XPATH))
        )
        return job_title.text

    def close_the_job(self):
        try:
            self.click_on_post_card_options_button()
            self.select_remove_post_option()
            self.dropdown_reasons_of_the_delete()
            self.select_a_reason_for_remove()
            self.click_on_close_job_button()
            return True
        except Exception as e:
            print(e)
            return False

    def edit_the_job_post(self):
        self.click_on_post_card_options_button()
        self.select_edit_post_option()
        self.edit_post_title_option()
        self.change_the_title_of_post()
        self.click_on_save()
        self.click_on_save_the_post()
