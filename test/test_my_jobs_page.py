import concurrent.futures
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wraper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.main_page import MainPage
from logic.my_jobs_page import MyJobsPage
from logic.post_job_page import PostJobPage
from logic.setting_page import SettingPage


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def test_close_a_job(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.post_job_button()
        post_job_page = PostJobPage(driver)
        post_job_page.post_new_job()
        post_job_page.navigate_to_my_jobs_page()
        my_jobs_page = MyJobsPage(driver)
        bol = my_jobs_page.close_the_job()
        driver.quit()
        self.assertTrue(bol)

    def test_edit_job_post(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.post_job_button()
        post_job_page = PostJobPage(driver)
        post_job_page.post_new_job()
        post_job_page.navigate_to_my_jobs_page()
        my_jobs_page = MyJobsPage(driver)
        my_jobs_page.edit_the_job_post()
        new_title = my_jobs_page.get_job_title()
        driver.quit()
        self.assertEqual(new_title, "New title")

    def test_specific_test(self):
        self.browser_wrapper.run_test(self.test_close_a_job)  # select the specific function you want to run

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_edit_job_post, self.test_close_a_job]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()
