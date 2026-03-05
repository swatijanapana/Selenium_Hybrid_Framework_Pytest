import pytest

from Pages.LoginPage import LoginPage
from Utilities.config_reader import get_config

@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def setup_method(self):
       self.config = get_config()

    def login_and_get_home(self):
        self.loginPage = LoginPage(self.driver)
        username = self.config["CREDENTIALS"]["USERNAME"]
        password = self.config["CREDENTIALS"]["PASSWORD"]
        return self.loginPage.do_login(username, password)

