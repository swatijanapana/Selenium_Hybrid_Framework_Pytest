import pytest
from Constants import constants
from Pages.LoginPage import LoginPage
from Utilities.excel_reader import get_login_data


@pytest.mark.parametrize("scenario,username,password,expected", get_login_data())
def test_login_from_excel(driver,scenario,username,password,expected):
    loginPage = LoginPage(driver)

    username = username or ""
    password = password or ""

    homePage = loginPage.do_login(username, password)

    if expected == "PASS":
        # After successful login, title should be home page title
        assert  homePage.get_title(constants.HOME_PAGE_TITLE) == constants.HOME_PAGE_TITLE
    else:
        # Blank fields -> field validation ("Required")
        if username == "" or password == "":
            if username == "":
                assert loginPage.get_username_required_text() == "Required"
            if password == "":
                assert loginPage.get_password_required_text() == "Required"
        else:
            assert loginPage.get_error_message() == "Invalid credentials"

