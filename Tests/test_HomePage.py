import Constants.constants as constants
from Tests.test_BasePage import BaseTest


class Test_Home(BaseTest):


    def test_home_page_title(self):
        homePage = self.login_and_get_home()
        homepage_title =  homePage.get_home_page_title(constants.HOME_PAGE_TITLE)
        assert homepage_title == constants.HOME_PAGE_TITLE


    def test_home_page_header_value_dashboard(self):
        self.homePage = self.login_and_get_home()
        header_value = self.homePage.get_header_value()
        assert header_value == "Dashboard"

    def test_orangehrm_logo_exist(self):
        self.homePage = self.login_and_get_home()
        assert  self.homePage.is_logo_exist()

    def test_profile_icon_exist(self):
        self.homePage = self.login_and_get_home()
        assert  self.homePage.is_profile_picture_exist()


    def test_left_menu_visible(self):
        self.homePage = self.login_and_get_home()
        assert self.homePage.is_menu_list_exist()

    def test_menu_items_match_expected(self):
        self.homePage = self.login_and_get_home()
        actual_menu = self.homePage.get_menu_items_text()
        expected_menu = ["Admin","PIM","Leave","Time", "Recruitment","My Info","Performance", "Dashboard","Directory",
                         "Maintenance", "Claim", "Buzz" ]
        for item in expected_menu:
            assert item in actual_menu


    def test_click_admin_menu(self):
        self.homePage = self.login_and_get_home()
        self.homePage.click_admin_menu()
        assert self.homePage.get_header_value() == constants.ADMIN_PAGE_HEADER_VALUE

    def test_click_myinfo_menu(self):
        self.homePage = self.login_and_get_home()
        self.homePage.click_myinfo_menu()
        assert self.homePage.get_header_value() == constants.MYINFO_PAGE_HEADER_VALUE

    def test_logout(self):
        self.homePage = self.login_and_get_home()
        self.homePage.do_logout()
        assert self.driver.title == constants.LOGIN_PAGE_TITLE



