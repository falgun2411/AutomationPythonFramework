# about conftest.py file
# The fixtures that you will define in this file, will be shared among all tests in your test suite

import pytest
from utils import utils as utils
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.ie.options import Options
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser n(me e.g.chrome OR firefox")

# by default scope is at "function" level, so browser will invoke every time , for new function
# currently we are keeping scope at "class" level so browser will invoke once
# and run all the tests within the class one by one. So,  Test2 will start, where TEST1 was ended


@pytest.fixture(scope="class")
def test_setup(request):
    # we are defining "request" instead of "self"
    print("**********   Test execution is started.   **********")
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    # passing the parameters to use the correct browser

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=utils.CHROME_DriverPath)
    elif browser == 'firefox':
        binary = r'utils.FIREFOX_DriverPath'
        fp = (r'C:\Users\username\AppData\Roaming\Mozilla\Firefox\Profiles\oqmqnsih.default')
        opts = Options()
        opts.profile = fp
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        fp.__setattr__("javascript.enabled", False)
        driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_binary=binary, firefox_options=opts)
    elif browser == 'IE':
        ie_driver = r'utils.IE_DriverPath'
        opts = Options()
        opts.ignore_protected_mode_settings = True
        opts.ignore_zoom_level = True
        opts.require_window_focus = True
        opts.set_preference("javascript.enabled", False)
        driver = webdriver.Ie(ie_driver, ie_options=opts)


    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    # adding this, and this driver will be sent to all the classes, in class we will all one more fixture.
    # --@pytest.mark.usefixtures
    yield
    driver.close()
    driver.quit()
    print("**********   Test execution is completed successfully. **********")