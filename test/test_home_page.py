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

    def test_post_new_job(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.post_job_button()
        post_job_page = PostJobPage(driver)
        post_job_page.post_new_job()
        message = post_job_page.get_the_message_of_successfully_post()
        driver.quit()
        self.assertEqual(message, "Congratulations!")

    def test_page_load_time(self, driver):
        start_time = time.time()
        # Wait until document.readyState is complete
        WebDriverWait(driver, 10).until(
            lambda drive: driver.execute_script("return document.readyState") == "complete")
        end_time = time.time()
        load_time = end_time - start_time
        print("Page load time:", load_time, "seconds")
        driver.quit()
        self.assertLessEqual(load_time, 5, "Page load time exceeds 5 seconds")

    def test_search_suggestions_functionality(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.click_on_search_input_and_insert_text()
        result = home_page.check_dropdown_exist()
        driver.quit()
        self.assertTrue(result)

    def test_specific_test(self):
        self.browser_wrapper.run_test(self.test_post_new_job)  # select the specific function you want to run

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_page_load_time, self.test_post_new_job, self.test_search_suggestions_functionality]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()
