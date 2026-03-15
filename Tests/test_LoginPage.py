import Constants.constants as constants
from Pages.LoginPage import LoginPage
from Tests.test_BasePage import BaseTest


class  Test_Login(BaseTest):

    """ Login Page test cases. """


    def test_environment_health_check(self):
        """ Verify login page core elements are visible. """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_username_field_exist()
        assert self.loginPage.is_password_field_exist()
        assert self.loginPage.is_login_button_exist()


    def test_login_page_title(self):
        """ Verify login page title is displayed correctly. """
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(constants.LOGIN_PAGE_TITLE)
        assert title == constants.LOGIN_PAGE_TITLE


    def test_login(self):
        """ Verify user can log in with valid credentials. """
        self.loginPage = LoginPage(self.driver)
        username = self.config["CREDENTIALS"]["USERNAME"]
        password = self.config["CREDENTIALS"]["PASSWORD"]
        self.homePage = self.loginPage.do_login(username,password)
        title = self.homePage.get_title(constants.HOME_PAGE_TITLE)
        assert title == constants.HOME_PAGE_TITLE


    def test_forgot_password_link_visible(self):
        """ Verify forgot password link is visible on login page. """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_forgot_password_link_exist()


    def test_username_required_exist(self):
        """ Verify username required message is displayed when username is empty. """
        self.loginPage = LoginPage(self.driver)
        password = self.config["CREDENTIALS"]["PASSWORD"]
        self.loginPage.do_login("", password)
        assert  self.loginPage.is_username_required_exist()


    def test_password_required_exist(self):
        """ Verify password required message is displayed when username is empty. """
        self.loginPage = LoginPage(self.driver)
        username = self.config["CREDENTIALS"]["USERNAME"]
        self.loginPage.do_login(username, "")
        assert self.loginPage.is_password_required_exist()






