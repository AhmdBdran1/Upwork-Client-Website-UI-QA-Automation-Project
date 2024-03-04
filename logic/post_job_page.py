from time import sleep
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostJobPage(BasePage):  # logic class for post job page
    SHORT_TERM_PROJECT_SELECTION_XPATH = "//*[@id='main']/div[3]/div[4]/div[1]/section/div/div[2]/div/div/div[1]/div/div/div/div/div/fieldset/div/div[2]/div"
    NEXT_AFTER_SELECT_THE_LONG_TERM = "//*[@id='main']/div[3]/div[4]/div[2]/div/button[2]"
    ACCEPT_ALL_COOKIES_BTN_XPATH = "//*[@id='onetrust-accept-btn-handler']"
    DO_POST_WITHOUT_AI_XPATH = "//*[@id='main']/div[2]/div[5]/div[2]/div[1]/button[2]"
    INPUT_TITLE_OF_JOB_POST_XPATH = "//*[@id='job-post-title']"
    NEXT_TO_SKILLS_BTN_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[2]/div[2]/button[2]"
    ADD_FIREBASE_TO_REQUIRED_SKILLS_XPATH = "//*[@id='cardCollapse-']/div/div/div/div/div[1]"
    ADD_FLUTTER_TO_REQUIRED_SKILLS_XPATH = "//*[@id='cardCollapse-']/div/div/div/div/div[1]"
    NEXT_TO_SCOPE_BUTTON_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[2]/div[2]/button[2]"
    SELECT_THE_SIZE_OF_THE_PROJECT_AS_SMALL_BTN_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div[4]/label/span"
    SELECT_THE_TIME_OF_THE_PROJECT_AS_LESS_THAN_MONTH_BTN_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div[2]/label[3]/span[1]"
    SELECT_THE_LEVEL_OF_THE_PROJECT_AS_ENTRY_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div/div/div[3]/label[1]/span"
    NO_HIRE_CHANCE_BTN_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/div[4]/div/div/div[2]/label/span[1]"
    NEXT_TO_THE_BUDGET_BTN_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[2]/div[2]/button[2]"
    SELECT_THE_FIXED_PRICE_OPTION_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div/fieldset/div/div[2]/div"
    INPUT_THE_FIXED_PRICE = "//*[@id='fixed-price-input']"
    NEXT_TO_DESCRIPTION_XPATH = "//*[@id='main']/div[3]/div[5]/div/div[2]/div[2]/div[2]/div[2]/button[2]"
    INPUT_DESCRIPTION_XPATH = "//*[@id='jp-description-1']"
    NEXT_TO_REVIEW_XPATH = "//*[@id='main']/div[2]/div[5]/div/div[2]/div/div[2]/div[2]/button[2]"
    POST_THE_JOB_AFTER_REVIEW_BTN = "//*[@id='main']/div[3]/div[4]/div[3]/button"
    NO_THANKS_XPATH = "/html/body/div[8]/div/div[2]/div/div/div[2]/div[2]/div[2]/button[1]"
    MESSAGE_OF_SUCCESSFULLY_POST = "//*[@id='main']/div[2]/div[4]/div/div/div[1]/div[2]/div/strong"
    NAVIGATE_TO_MY_JOBS_PAGE_XPATH = "//*[@id='user-top-navigation-container']/header/div/div[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def accept_cookies(self):  # function that try to locate the cookies , and accept it
        try:
            accept_all_cookies = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.ACCEPT_ALL_COOKIES_BTN_XPATH))
            )
            accept_all_cookies.click()

        except Exception as e:
            print("there is no cookies to accept:")
            print(e)

    def select_short_term_project(self):  # function that select short term project inside the post new job process
        short_term_project_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SHORT_TERM_PROJECT_SELECTION_XPATH))
        )
        short_term_project_btn.click()

    def click_continue(self):  # function that click on continue inside the post job process
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_AFTER_SELECT_THE_LONG_TERM))
        )
        continue_btn.click()

    def insert_job_post_title(self):  # function that insert job post title inside the post job process
        input_title_of_job_post = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_TITLE_OF_JOB_POST_XPATH))
        )
        input_title_of_job_post.send_keys("Flutter Developer Needed for Firebase Integration Assistance")

    def click_on_continue_to_skills(self):  # function that click on continue to skills inside the post job process
        next_to_skills_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_TO_SKILLS_BTN_XPATH))
        )
        next_to_skills_btn.click()

    def add_required_skills_for_job(self):  # function that add required skills inside the post job process
        add_firebase_to_required_skills = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_FIREBASE_TO_REQUIRED_SKILLS_XPATH))
        )
        add_firebase_to_required_skills.click()
        sleep(2)
        add_flutter_to_required_skills = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_FLUTTER_TO_REQUIRED_SKILLS_XPATH))
        )
        add_flutter_to_required_skills.click()

    def click_to_continue_to_scope(self):  # function that click to continue to scope inside the post job process
        next_to_scope_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_TO_SCOPE_BUTTON_XPATH))
        )
        next_to_scope_button.click()

    def select_size_of_the_project(self):  # function that select size of the project inside the post job process
        size_of_the_project_as_small = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_THE_SIZE_OF_THE_PROJECT_AS_SMALL_BTN_XPATH))
        )
        size_of_the_project_as_small.click()

    def select_the_time_of_the_project(self):  # function that select the time needed  inside the post job process
        time_of_the_project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_THE_TIME_OF_THE_PROJECT_AS_LESS_THAN_MONTH_BTN_XPATH))
        )
        time_of_the_project.click()

    def select_the_level_of_the_project(self):  # function that select the level of the project inside the post job
        # process
        level_of_the_project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_THE_LEVEL_OF_THE_PROJECT_AS_ENTRY_XPATH))
        )
        level_of_the_project.click()

    def select_if_there_is_opportunity_to_hire(self):  # function that select if there is opportunity to hire inside
        # the post job process
        no_hire_chance_opportunity = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NO_HIRE_CHANCE_BTN_XPATH))
        )
        no_hire_chance_opportunity.click()

    def click_to_continue_to_budget_section(self):  # function that click to continue to budget section inside the
        # post job process
        continue_to_budget_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_TO_THE_BUDGET_BTN_XPATH))
        )
        continue_to_budget_btn.click()

    def click_to_choose_the_fixed_price_option(self):  # function that click to choose fixed price inside the post job
        # process
        fixed_price_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_THE_FIXED_PRICE_OPTION_XPATH))
        )
        fixed_price_option.click()

    def input_the_fixed_price(self):  # function that input the fixed price inside the post job process
        input_fixed_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_THE_FIXED_PRICE))
        )
        input_fixed_price.send_keys("5")

    def click_to_continue_to_description(self):  # function that click on continue to description inside the post job
        # process
        continue_to_description_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_TO_DESCRIPTION_XPATH))
        )
        continue_to_description_button.click()

    def insert_description(self):  # function that insert description inside the post job process
        input_description = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_DESCRIPTION_XPATH))
        )
        input_description.send_keys(
            "We are seeking a skilled Flutter developer with expertise in Firebase integration to link our Flutter mobile application with Firebase backend services. The ideal candidate should have experience in connecting Flutter apps with Firebase Authentication, Firestore, Cloud Functions, and Cloud Storage. This project requires seamless integration to ensure smooth data flow and authentication processes between the app and Firebase services. If you have a proven track record of successful Firebase integrations and are proficient in Flutter development, we'd love to hear from you! Please provide examples of previous work showcasing your Firebase and Flutter expertise.")

    def click_to_continue_to_review(self):  # function that click on continue to review inside the post job process
        continue_to_review_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_TO_REVIEW_XPATH))
        )
        continue_to_review_button.click()

    def click_to_post_the_job(self):  # function that click on "post job" inside the post job process
        post_job_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.POST_THE_JOB_AFTER_REVIEW_BTN))
        )
        post_job_button.click()

    def click_no_thanks_button(self):  # function that click on "no thanks" inside the post job process
        button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_THANKS_XPATH))
        )
        button.click()

    def get_the_message_of_successfully_post(self):  # function that get the message inside the post job process
        message_test_view = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.MESSAGE_OF_SUCCESSFULLY_POST))
        )
        return message_test_view.text

    def navigate_to_my_jobs_page(self):  # function that navigate to the jobs page
        navigate_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NAVIGATE_TO_MY_JOBS_PAGE_XPATH))
        )
        navigate_btn.click()

    def post_new_job(self):  # here we do all the actions needed to post a new job

        self.select_short_term_project()
        self.click_continue()
        self.accept_cookies()
        self.insert_job_post_title()
        self.click_on_continue_to_skills()
        self.add_required_skills_for_job()
        self.click_to_continue_to_scope()
        self.select_size_of_the_project()
        self.select_the_time_of_the_project()
        self.select_the_level_of_the_project()
        self.select_if_there_is_opportunity_to_hire()
        self.click_to_continue_to_budget_section()
        self.click_to_choose_the_fixed_price_option()
        self.input_the_fixed_price()
        self.click_to_continue_to_description()
        self.insert_description()
        self.click_to_continue_to_review()
        self.click_to_post_the_job()
        self.click_no_thanks_button()
