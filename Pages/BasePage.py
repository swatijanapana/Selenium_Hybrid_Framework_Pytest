from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages and contain all the generic methods and utilities for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """ Click an element after waiting until it is clickable. """
    def do_click(self, by_locator):
        element = WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(by_locator)).click()

    """ Enter text into an input field. """
    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver,60).until(EC.presence_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    """ Return the visible text of the element. """
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """ Return True if the element is visible. """
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """ Get the title of the element. """
    def get_title(self, title= None):
        if title:
          WebDriverWait(self.driver,50).until(EC.title_is(title))
        return self.driver.title

    """ Clear the existing value from an input field."""
    def do_clear(self,by_locator):
        element =  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        element.click()
        element.send_keys(Keys.COMMAND, "a")
        element.send_keys(Keys.BACKSPACE)

    """ Wait until the element becomes visible."""
    def wait_for_visibility(self,by_locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(by_locator))

    """ Wait until the page loader disappears."""
    def wait_for_loader_to_disappear(self,by_locator):
         WebDriverWait(self.driver,20).until(EC.invisibility_of_element_located(by_locator))

    """ Return True if the element is selected. """
    def is_selected(self,by_locator):
        element = WebDriverWait(self.driver,15).until(EC.presence_of_element_located(by_locator))
        return element.is_selected()

    """ Return the value of a specified property of the element."""
    def get_element_property(self, by_locator, property_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator)
        )
        return element.get_property(property_name)

    """ Verify element is checked or not"""
    def is_checked(self,by_locator):
       return self.get_element_property(by_locator,"checked")

    """ Wait until the element is clickable or not. """
    def wait_for_element_clickable(self,by_locator):
        return WebDriverWait(self.driver,10).until((EC.element_to_be_clickable(by_locator)))

    """ Refresh the page. """
    def refresh_page(self):
        self.driver.refresh()

    """ Click an element using JavaScript when normal click fails."""
    def js_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    """ Return the WebElement located by the locator."""
    def get_element(self,by_locator):
        return self.driver.find_element(*by_locator)

    """ Verify element is enabled or not"""
    def is_enabled(self,by_locator):
        element =  WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator))
        return element.is_enabled()

    """ Upload a file by sending the file path to a file input element."""
    def do_send_file(self, by_locator, file_path):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        element.send_keys(file_path)




