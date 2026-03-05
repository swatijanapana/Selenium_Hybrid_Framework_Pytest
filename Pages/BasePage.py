from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages and contain all the generic methods and utilites for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        element = WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title= None):
        if title:
          WebDriverWait(self.driver,50).until(EC.title_is(title))
        return self.driver.title

    def do_clear(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).clear()


    def wait_for_visibility(self,by_locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(by_locator))
