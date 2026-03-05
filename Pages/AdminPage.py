from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import Select


class AdminPage(BasePage):
    """ By Locators -- OR"""

    # User Management Tab
    User_management_tab = (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and text()= 'User Management ']")
    Add_button = (By.XPATH,"//button[@type='button' and text()=' Add ']")
    Search_button = (By.XPATH,"//button[@type='submit' and text()= ' Search ']")
    Reset_button = (By.XPATH,"//button[@type='button' and text()= ' Reset ']")
    Username_input = (By.XPATH,"//label[normalize-space()= 'Username']/following::input[1]")
    Result_table = (By.XPATH,"//div[@class='oxd-table-body']")
    Result_rows = (By.XPATH,"//div[@class='oxd-table-body']/child::div")
    No_Record_found_message = (By.XPATH,"//span[@class='oxd-text oxd-text--span' and text()='No Records Found']")
    User_role_dropdown = (By.XPATH, "//label[text()='User Role']/following::div[1]")
    Status_dropdown = (By.XPATH,"//label[text()='Status']/following::div[1]")


    """ Constructor of page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions for Admin Page """

    # User Management Tab
    """ Used to check the User_management tab is selected by default """

    def is_user_management_tab_selected(self):
        return self.is_visible(self.User_management_tab)

    """ Used to check the Add button exist """

    def is_add_button_exist(self):
        return self.is_visible(self.Add_button)

    """ Used to check the Search button exist """
    def is_search_button_exist(self):
        return self.is_visible(self.Search_button)

    """ Used to check the Reset button exist """
    def is_reset_button_exist(self):
        return self.is_visible(self.Reset_button)


    """ Used to input the Username """
    def enter_username(self,username):
        self.do_clear(self.Username_input)
        self.do_send_keys(self.Username_input,username)

    """ Used to retrieve the value from Username field """
    def get_username_value(self):
        element = self.driver.find_element(*self.Username_input)
        return element.get_attribute("value")

    """ Used to retrieve the value from User role dropdown """

    def get_userrole_selected_text(self):
        element = self.driver.find_element(*self.User_role_dropdown)
        return element.text

    """ Used to retrieve the value from Status  dropdown """

    def get_status_selected_text(self):
        element = self.driver.find_element(*self.Status_dropdown)
        return element.text

    """ Used to check entered  value in  Username field  appears in result table"""

    def is_username_present_results(self,username):
        table_text = self.driver.find_element(*self.Result_table).text
        return username in table_text

    """ Used to click the Search button"""
    def click_search_button(self):
        return self.do_click(self.Search_button)

    """ Used to click the Reset button"""
    def click_reset_button(self):
        return self.do_click(self.Reset_button)

    """ Used to check the No record found message displayed or not """

    def is_no_record_found_message_displayed(self):
        return self.is_visible(self.No_Record_found_message)

    """ Used to select item from dropdown"""

    def select_from_dropdown(self,dropdown_locator,option_text):
        #click dropdown
        self.do_click(dropdown_locator)
        #select option  with matching visible text
        option = (By.XPATH,f"//div[normalize-space()='{option_text}']")
        self.do_click(option)

    """ Used to count the total rows in results table"""
    def get_row_result_count(self):
        rows = self.driver.find_elements(*self.Result_rows)
        return len(rows)






