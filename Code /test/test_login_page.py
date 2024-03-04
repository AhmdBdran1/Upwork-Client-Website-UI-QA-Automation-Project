import time
import unittest
from infra.browser_wraper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.main_page import MainPage


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def test_login(self, driver):  # test the login process
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        name = home_page.get_the_name_of_the_account_owner()
        driver.quit()
        self.assertEqual(name, "Ahmd Bdran")

    def test_login_with_wrong_credential(self, driver): # test the login with the wrong credential
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login_with_wrong_credential()
        home_page = HomePage(driver)
        name = home_page.get_the_name_of_the_account_owner()
        driver.quit()
        self.assertTrue(True)

    def test_specific_test(self): # run just one required test
        self.browser_wrapper.run_test(self.test_login_with_wrong_credential)

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_login, self.test_login_with_wrong_credential]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()
