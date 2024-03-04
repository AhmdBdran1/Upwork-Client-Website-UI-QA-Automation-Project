import unittest
from infra.browser_wraper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.main_page import MainPage
from logic.setting_page import SettingPage


class HomePageTests(unittest.TestCase):  # test the home page , it's personal page after the user logged in

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def test_change_password_with_wrong_confirm_password(self, driver):  # test change the password with wrong
        # confirmation
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.navigate_to_setting_page()
        setting_page = SettingPage(driver)
        setting_page.change_current_password()
        message = setting_page.get_confirm_password_message()
        driver.quit()
        self.assertEqual(message, "Passwords do not match")

    def test_specific_test(self):
        self.browser_wrapper.run_test(self.test_change_password_with_wrong_confirm_password)  # select the specific
        # function you want to run

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_change_password_with_wrong_confirm_password]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()
