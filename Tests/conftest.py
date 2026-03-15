import pytest
from selenium import webdriver

# CLASS-BASED DRIVER FIXTURE
# Attaches driver to test class using request.cls.driver
# Used when tests inherit from BaseTest and access self.driver
@pytest.fixture(params=["chrome", "firefox", "edge"], scope='function')
def init_driver(request):

    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    if request.param == 'edge':
        web_driver = webdriver.Edge()

    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)

    yield
    web_driver.quit()

# FUNCTION-BASED DRIVER FIXTURE
# Returns driver directly to test functions
# Used when tests accept driver as a parameter

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    if request.param == 'edge':
        driver = webdriver.Edge()
    yield driver
    driver.quit()


