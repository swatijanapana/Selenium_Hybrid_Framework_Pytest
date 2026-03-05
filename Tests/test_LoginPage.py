import Constants.constants as constants
from Pages.LoginPage import LoginPage
from Tests.test_BasePage import BaseTest



class  Test_Login(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(constants.LOGIN_PAGE_TITLE)
        assert title == constants.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        username = self.config["CREDENTIALS"]["USERNAME"]
        password = self.config["CREDENTIALS"]["PASSWORD"]
        self.homePage = self.loginPage.do_login(username,password)
        title = self.homePage.get_title(constants.HOME_PAGE_TITLE)
        assert title == constants.HOME_PAGE_TITLE

    def test_forgot_password_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_forgot_password_link_exist()

    def test_logo_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_logo_exist()

    def test_invalid_login_wrong_password(self):
        self.loginPage = LoginPage(self.driver)
        username = self.config["CREDENTIALS"]["USERNAME"]
        self.loginPage.do_login(username, "wrong123")
        assert self.loginPage.get_error_message() == "Invalid credentials"

    def test_invalid_login_wrong_username(self):
        self.loginPage = LoginPage(self.driver)
        password = self.config["CREDENTIALS"]["PASSWORD"]
        self.loginPage.do_login("WrongUser", password)
        assert self.loginPage.get_error_message() == "Invalid credentials"

    def test_invalid_login_blank_field(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("", "")
        assert self.loginPage.get_username_required_text() == "Required"
        assert  self.loginPage.get_password_required_text() == "Required"


    def test_login_button_exist(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_login_button_exist()

    def test_login_button_enabled(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_login_button_enabled()

    def test_username_field_exist(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_username_field_exist()

    def test_password_field_exist(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_password_field_exist()

    def test_username_required_exist(self):
        self.loginPage = LoginPage(self.driver)
        password = self.config["CREDENTIALS"]["PASSWORD"]
        self.loginPage.do_login("", password)
        assert  self.loginPage.is_username_required_exist()

    def test_password_required_exist(self):
        self.loginPage = LoginPage(self.driver)
        username = self.config["CREDENTIALS"]["USERNAME"]
        self.loginPage.do_login(username, "")
        assert self.loginPage.is_password_required_exist()






