from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
import pytest
from pages.homePage import HomePage
from utils import utils as utils

# THIS IS DEMO FAKE TEST TO CHECK THE ADDITIONAL TEST CASES CAN BE ADDED LATER
@pytest.mark.usefixtures("test_setup")
class TestFakeReg():

    def test_demotest1(self):
        driver = self.driver
        driver.get(utils.URL)
        print( "Just to check other test case run...Demo")
