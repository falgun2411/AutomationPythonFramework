from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# This is search page user enters their financial institution to apply with


class SearchPage():

    def __init__(self, driver):
        # xapth used for this page
        self.driver = driver
        self.id_textinput_companyname= "companyName"
        self.SearchKeyword_for_comapany = "FinCompare GmbH"
        # creating dynamic Xpath based on keyword of search
        self.xpath_searched_comapnyName = "//h3[contains(.,'" + self.SearchKeyword_for_comapany + "')]"

    # Method to enter company name: Here we can add more company names in different format to verify results
    # Also one additional method will be needed later to check the SUBMIT Button behaviour once company name is entered
    def enter_companyName(self, SearchKeyword_for_comapany):
        print("Entering the Company Name")
        element_present = EC.presence_of_element_located((By.ID, self.id_textinput_companyname))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_id(self.id_textinput_companyname).click()
        self.driver.find_element_by_id(self.id_textinput_companyname).clear()
        self.driver.find_element_by_id(self.id_textinput_companyname).send_keys(SearchKeyword_for_comapany)
        print("Company Name is entered........OK")

    # method to get  and return the page details , return type: string
    def get_page_title(self):
        ActualTitle = self.driver.find_element_by_css_selector("h2.funnel__step__title").text
        return ActualTitle

    # method to Submit company details
    def submit_the_companyName(self):
        print("Submitting the Company Name form search")
        self.driver.find_element_by_id(self.id_textinput_companyname).submit()
        print("Company Name is submitted for search result........OK")

    # method to Select company Name from search results
    # Later we can create different method to identify the number of search result from the list and select accordingly
    def select_comapny_from_searchresult(self, SearchKeyword_for_comapany):
        print("Selecting Company Name form search result")
        dynamic_xpath_for_searched_comapnyName = "//h3[contains(.,'" + self.SearchKeyword_for_comapany + "')]"
        element_present = EC.presence_of_element_located((By.XPATH, dynamic_xpath_for_searched_comapnyName))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_xpath(dynamic_xpath_for_searched_comapnyName).click()
        print("Company Name is selected form search result........OK")

