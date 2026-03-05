from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage
from Utilities.config_reader import get_config

class LoginPage(BasePage):

    """ By Locators -- OR"""
    Username = (By.NAME, "username")
    Password = (By.NAME, "password")
    Login_button = (By.CSS_SELECTOR, "button.orangehrm-login-button")
    Forgot_password_link = (By.CSS_SELECTOR, "p.orangehrm-login-forgot-header")
    Error_message = (By.CSS_SELECTOR, "p.oxd-alert-content-text")
    Logo_icon = (By.CLASS_NAME, "orangehrm-login-logo")
    Username_required = (By.XPATH,"//input[@name='username']/ancestor::div[contains(@class,'oxd-input-group')]//span[normalize-space()='Required']")
    Password_required = (By.XPATH,"//input[@name='password']/ancestor::div[contains(@class,'oxd-input-group')]//span[normalize-space()='Required']")


    """ Constructor of page class"""
    def __init__(self, driver):
        super().__init__(driver)
        config = get_config()
        self.driver.get(config["BASE_URL"])

    """ Page Actions for Login Page """

    """ Used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """ Used to check the forgot password link"""
    def is_forgot_password_link_exist(self):
        return self.is_visible(self.Forgot_password_link)

    """ Used to login the website"""
    def do_login(self,username,password):
        self.do_send_keys(self.Username,username)
        self.do_send_keys(self.Password,password)
        self.do_click(self.Login_button)
        return HomePage(self.driver)

    """ Used to get the error message"""
    def get_error_message(self):
        return self.get_element_text(self.Error_message)

    """ Used to verify the logo """
    def is_logo_exist(self):
        return self.is_visible(self.Logo_icon)

    """ Used to verify the login button exist """
    def is_login_button_exist(self):
        return self.is_visible(self.Login_button)

    """ Used to verify the login button enabled """
    def is_login_button_enabled(self):
        element = self.driver.find_element(*self.Login_button)
        return element.is_enabled()

    """ Used to verify the username field exist """
    def is_username_field_exist(self):
        return self.is_visible(self.Username)

    """ Used to verify the password field  exist """
    def is_password_field_exist(self):
        return self.is_visible(self.Password)

    """ Used to verify username_required  message exist"""
    def is_username_required_exist(self):
        return self.is_visible(self.Username_required)

    """ Used to verify password_required  message exist"""
    def is_password_required_exist(self):
        return self.is_visible(self.Password_required)

    """ Used to verify username_required_text message"""
    def get_username_required_text(self):
        return self.get_element_text(self.Username_required)

    """ Used to verify password_required_text message"""
    def get_password_required_text(self):
        return self.get_element_text(self.Password_required)




