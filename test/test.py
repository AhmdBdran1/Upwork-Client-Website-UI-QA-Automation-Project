import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wraper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.my_jobs_page import MyJobsPage
from logic.post_job_page import PostJobPage
from logic.setting_page import SettingPage


class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def test_login(self, driver):  # test the login process
        login_page = LoginPage(driver)
        Home_page = HomePage(driver)
        Home_page.click_to_start_login()
        login_page.login()
        name = Home_page.get_the_name_of_the_account_owner()
        print(name)
        self.assertEqual(name, "Ahmd Bdran")

    def test_post_new_job(self, driver):
        login_page = LoginPage(driver)
        Home_page = HomePage(driver)
        Home_page.click_to_start_login()
        login_page.login()
        Home_page.post_job_button()
        post_job_page = PostJobPage(driver)
        post_job_page.post_new_job()
        message = post_job_page.get_the_message_of_successfully_post()
        self.assertEqual(message, "Congratulations!")

    def test_change_password_with_wrong_confirm_password(self, driver):
        login_page = LoginPage(driver)
        Home_page = HomePage(driver)
        Home_page.click_to_start_login()
        login_page.login()
        Home_page.navigate_to_setting_page()
        setting_page = SettingPage(driver)
        setting_page.change_current_password()
        message = setting_page.get_confirm_password_message()
        self.assertEqual(message, "Passwords do not match")

    def test_page_load_time(self, driver):
        start_time = time.time()
        # Wait until document.readyState is complete
        WebDriverWait(driver, 10).until(
            lambda drive: driver.execute_script("return document.readyState") == "complete")
        end_time = time.time()
        load_time = end_time - start_time
        print("Page load time:", load_time, "seconds")
        self.assertLessEqual(load_time, 5, "Page load time exceeds 5 seconds")

    def test_close_a_job(self, driver):
        login_page = LoginPage(driver)
        Home_page = HomePage(driver)
        Home_page.click_to_start_login()
        login_page.login()
        Home_page.post_job_button()
        post_job_page = PostJobPage(driver)
        post_job_page.post_new_job()
        post_job_page.navigate_to_my_jobs_page()
        my_jobs_page = MyJobsPage(driver)
        bol = my_jobs_page.close_the_job()
        self.assertTrue(bol)

    def test_edit_job_post(self,driver):
        login_page = LoginPage(driver)
        Home_page = HomePage(driver)
        Home_page.click_to_start_login()
        login_page.login()
        Home_page.post_job_button()
        post_job_page = PostJobPage(driver)
        post_job_page.post_new_job()
        post_job_page.navigate_to_my_jobs_page()
        my_jobs_page = MyJobsPage(driver)
        my_jobs_page.edit_the_job_post()
        new_title = my_jobs_page.get_job_title()
        self.assertEqual(new_title, "New title")

    def test_specific_test(self):
        self.browser.run_test(self.test_post_new_job)  # select the specific function you want to run

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_login,self.test_page_load_time,self.test_post_new_job,self.test_edit_job_post,
                      self.test_change_password_with_wrong_confirm_password, self.test_close_a_job]
        for test in tests_list:
            self.browser.run_test(test)


if __name__ == "__main__":
    unittest.main()
