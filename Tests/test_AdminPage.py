from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants import constants as constants
from TestData.testdata import ADMIN_TESTDATA
from Tests.test_BasePage import BaseTest

class Test_Admin(BaseTest):

    def admin_menu_login(self):
        self.homePage = self.login_and_get_home()
        adminPage = self.homePage.click_admin_menu()
        return adminPage

    def test_user_management_tab_selected(self):
        self.adminPage = self.admin_menu_login()
        assert self.adminPage.is_user_management_tab_selected()

    def test_add_button_visible(self):
        self.adminPage = self.admin_menu_login()
        assert self.adminPage.is_add_button_exist()

    def test_reset_button_visible(self):
        self.adminPage = self.admin_menu_login()
        assert self.adminPage.is_reset_button_exist()

    def test_search_button_visible(self):
        self.adminPage = self.admin_menu_login()
        assert self.adminPage.is_search_button_exist()

    def test_search_with_valid_username(self):
        self.adminPage = self.admin_menu_login()
        test_value = ADMIN_TESTDATA["valid_username"]
        self.adminPage.enter_username(test_value)
        self.adminPage.click_search_button()
        assert self.adminPage.is_username_present_results(test_value)

    def test_input_username_field(self):
        self.adminPage = self.admin_menu_login()
        test_value = ADMIN_TESTDATA["input_username"]
        self.adminPage.enter_username(test_value)
        assert self.adminPage.get_username_value() == test_value

    def test_search_with_invalid_username(self):
        self.adminPage = self.admin_menu_login()
        invalid_username_value = ADMIN_TESTDATA["invalid_username"]
        self.adminPage.enter_username(invalid_username_value)
        self.adminPage.click_search_button()
        self.adminPage.wait_for_visibility(self.adminPage.No_Record_found_message,timeout= 50)
        self.driver.save_screenshot("Reports/Screenshots/invalid_search.png")
        assert self.adminPage.is_no_record_found_message_displayed()

    def test_click_reset_button(self):
        self.adminPage = self.admin_menu_login()
        self.adminPage.click_reset_button()
        assert self.adminPage.get_username_value() == constants.USER_NAME_VALUE
        assert self.adminPage.get_userrole_selected_text() == constants.DEFAULT_DROPDOWN_TEXT
        assert self.adminPage.get_status_selected_text() == constants.DEFAULT_DROPDOWN_TEXT


    def test_select_from_userrole_dropdown(self):
        self.adminPage = self.admin_menu_login()
        option_text = ADMIN_TESTDATA["user_role_option_2"]
        self.adminPage.select_from_dropdown(self.adminPage.User_role_dropdown,option_text)
        assert self.adminPage.get_userrole_selected_text() == option_text

    def test_select_from_status_dropdown(self):
        self.adminPage = self.admin_menu_login()
        option_text = ADMIN_TESTDATA["status_option_1"]
        self.adminPage.select_from_dropdown(self.adminPage.Status_dropdown, option_text)
        assert self.adminPage.get_status_selected_text() == option_text

    def test_click_reset_clear_filters_after_search(self):
        self.adminPage = self.admin_menu_login()
        self.adminPage.click_reset_button()
        test_value = ADMIN_TESTDATA["valid_username"]
        self.adminPage.enter_username(test_value)
        option_text = ADMIN_TESTDATA["user_role_option_2"]
        self.adminPage.select_from_dropdown(self.adminPage.User_role_dropdown, option_text)
        option_text = ADMIN_TESTDATA["status_option_1"]
        self.adminPage.select_from_dropdown(self.adminPage.Status_dropdown, option_text)
        self.adminPage.click_search_button()
        row_count_after_search = self.adminPage.get_row_result_count()
        assert row_count_after_search > 0
        self.adminPage.wait_for_visibility(self.adminPage.Result_table)
        self.adminPage.click_reset_button()
        assert self.adminPage.get_username_value() == constants.USER_NAME_VALUE
        assert self.adminPage.get_userrole_selected_text() == constants.DEFAULT_DROPDOWN_TEXT
        assert self.adminPage.get_status_selected_text() == constants.DEFAULT_DROPDOWN_TEXT





