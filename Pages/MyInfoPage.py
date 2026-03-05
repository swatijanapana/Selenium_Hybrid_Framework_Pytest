from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class MyInfoPage(BasePage):
    """ By Locators -- OR"""

    Personal_details_menu = (By.XPATH, "//a[text()='Personal Details']")

    """ Constructor of page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions for MyInfo Page """

    """ Used to check the Personal Details Menu exist"""

    def click_personal_details_menu(self):
        return self.do_click(self.Personal_details_menu)

