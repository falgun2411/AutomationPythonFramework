from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# This is Leasing category Page, user enters the details for their lease details


class LeasingPage():

    def __init__(self, driver):
        # xapth used for this page
        self.driver = driver
        self.name_field_Amount = "amount"
        self.id_dropdown_assetCategory = "select-assetCategory"
        self.id_dropdown_assetType = "select-assetType"
        self.id_dropdown_Term = "select-term"
        self.xpath_button_type_submit = "//span[contains(.,'Weiter')]"

    # Method to enter amount
    # Later Scope: Need other Test Data set for amount entered and calculated , in DB + User side
    def enter_amount(self):
        print("entering amount(acquisition cost)")
        self.driver.find_element_by_name(self.name_field_Amount).clear()
        self.driver.find_element_by_name(self.name_field_Amount).send_keys("50000")
        print("amount(acquisition cost) is entered....OK")

    # method to get  and return the page details , return type: string
    def get_page_title(self):
        ActualTitle = self.driver.find_element_by_css_selector("h2.funnel__step__title").text
        return ActualTitle

    # Method: to enter Finance category
    # Later Scope: A dynamic method will be needed to check all drop down options and click from that option
    def enter_AssetCategory(self):
        print("Clicking drop down assetCategory(finance)")
        element_present = EC.element_to_be_clickable((By.ID, self.id_dropdown_assetCategory))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_id(self.id_dropdown_assetCategory).click()
        print("Selecting option:- Land und Forst")
        element_present = EC.presence_of_element_located((By.XPATH, "//li[contains(.,'Land und Forst')]"))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_xpath("//li[contains(.,'Land und Forst')]").click()
        print("Option Land und Forst is selected....OK")

    # Method: to enter Finance Sub category
    # Later Scope: A dynamic method will be needed to check all drop down options and click from that option
    def enter_AssetType(self):
        print("Clicking drop down assetType(subcategory)")
        element_present = EC.element_to_be_clickable((By.ID, self.id_dropdown_assetType))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_id(self.id_dropdown_assetType).click()
        print("Selecting option:- Lader")
        element_present = EC.presence_of_element_located((By.XPATH, "//li[contains(.,'Lader')]"))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_xpath("//li[contains(.,'Lader')]").click()
        print("Option:- Lader : is selected....OK")

    # Method: to enter Finance Term
    # Later Scope: A dynamic method will be needed to check all drop down options and click from that option
    def enter_AssetTerm(self):
        print("Clicking dropdown term(running time)")
        element_present = EC.element_to_be_clickable((By.ID, self.id_dropdown_Term))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_id(self.id_dropdown_Term).click()
        print("Selecting option:- 12 Monate")
        element_present = EC.presence_of_element_located((By.XPATH, "//li[contains(.,'12 Monate')]"))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_xpath("//li[contains(.,'12 Monate')]").click()
        print("Option:- 12 Monate : is selected.....OK")

    # Method: to submit the filled details
    # Additional for later: We can also use the double click event on button with Action Class
    def submit_details(self):
        print("Clicking submit button........")
        element_present = EC.presence_of_element_located((By.XPATH, self.xpath_button_type_submit))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_xpath(self.xpath_button_type_submit).click()
        print("Submit button is clicked....OK")
