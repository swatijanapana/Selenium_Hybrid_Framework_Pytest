import pytest

from Pages.LoginPage import LoginPage
from Utilities.config_reader import get_config

@pytest.mark.usefixtures("init_driver")
class BaseTest:

    """ Base test class for common test setup and login helpers. """

    driver = None
    loginPage = None
    config = None

    def setup_method(self):
        """ Load configuration before each test method. """
        self.config = get_config()

    def login_and_get_home(self):
        """ Log in with valid credentials and return Home page object. """
        self.loginPage = LoginPage(self.driver)
        username = self.config["CREDENTIALS"]["USERNAME"]
        password = self.config["CREDENTIALS"]["PASSWORD"]
        return self.loginPage.do_login(username, password)

