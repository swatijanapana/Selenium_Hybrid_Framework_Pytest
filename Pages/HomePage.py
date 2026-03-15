from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.AdminPage import AdminPage
from Pages.MyInfoPage import MyInfoPage


class HomePage(BasePage):

    """ By Locators -- OR"""

    HomePage_logo = (By.CSS_SELECTOR, "img[src='/web/images/orangehrm-logo.png?v=1763650546848']")
    Page_header = (By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']")
    Logout_button = (By.XPATH, "//a[text()='Logout']")
    Profile_dropdown = (By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    Profile_icon = (By.CLASS_NAME, "oxd-userdropdown-img")
    Menu_list = (By.CSS_SELECTOR, "ul.oxd-main-menu")
    Admin_menu= (By.XPATH,"//span[text()='Admin']")
    MyInfo_menu = (By.XPATH,"//span[text() ='My Info']")
    AdminPage_header = (By.CLASS_NAME,"oxd-topbar-header-title")


    """ Constructor of page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions for Dashboard Home Page """

    """ Returns the home page title. """
    def get_home_page_title(self,title):
        return self.get_title(title)

    """" Returns home page header. """

    def get_header_value(self):
       return self.get_element_text(self.Page_header)

    """ Verify page logo exist or not. """

    def is_logo_exist(self):
      return self.is_visible(self.HomePage_logo)

    """ Verify profile picture exist or not. """

    def is_profile_picture_exist(self):
      return self.is_visible(self.Profile_icon)

    """ Verify logout button visible or not"""
    def is_logout_button_exist(self, ):
       return self.is_visible(self.Logout_button)

    """ Verify menu_list. """
    def is_menu_list_exist(self):
        return self.is_visible(self.Menu_list)

    """ Returns the  menu_list text. """
    def get_menu_items_text(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR,"ul.oxd-main-menu span")
        return [element.text for element in elements]

    """ Verify admin_link is clickable or not. """
    def click_admin_menu(self):
        self.do_click(self.Admin_menu)
        return AdminPage(self.driver)

    """ Verify myinfo_link is  clickable or not. """
    def click_myinfo_menu(self):
        self.do_click(self.MyInfo_menu)
        return MyInfoPage(self.driver)

    """Log out from the application. """
    def do_logout(self):
        self.do_click(self.Profile_dropdown)
        self.do_click(self.Logout_button)






