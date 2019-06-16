from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# This is signup page user enters their details for registration


class SignUpPage():

    def __init__(self, driver):
        # xapth used for this page
        self.driver = driver
        self.id_textinput_firstName = "firstName"
        self.id_textinput_lastName = "lastName"
        self.id_textinput_email = "email"
        self.id_textinput_buisnessRelation = "select-businessRelation"
        self.xpath_Button_signupPage = "//span[contains(.,'Kostenlos registrieren')]"
        self.firstname = "testfirstName"
        self.lastname = "testLastname"
        self.email_address = "testemail"

    # method to enter First name ( We can create set of FirstName Test Data to enter and verify behaviour)
    def enter_firstname(self, firstname):
         print("Entering - FirstName.....")
         self.driver.find_element_by_id(self.id_textinput_firstName).click()
         self.driver.find_element_by_id(self.id_textinput_firstName).clear()
         self.driver.find_element_by_id(self.id_textinput_firstName).send_keys(firstname)
         print("First Name is entered.....OK")

    # method to enter Last Name
    def enter_lastname(self, lastname):
         print("Entering - LastName.....")
         self.driver.find_element_by_id(self.id_textinput_lastName).clear()
         self.driver.find_element_by_id(self.id_textinput_lastName).send_keys(lastname)
         print("Last Name is entered.....OK")

    # method to enter email address
    def enter_email(self, email_address):
         print("Entering EMail address")
         self.driver.find_element_by_id(self.id_textinput_email).clear()
         self.driver.find_element_by_id(self.id_textinput_email).send_keys(email_address+"@test.com")
         print("EMail address is entered.....OK")

    # method to select Business relation
    def enter_buisnessrelation(self):
         print("Selecting - Business Relation")
         self.driver.find_element_by_id(self.id_textinput_buisnessRelation).click()
         element_present = EC.presence_of_element_located((By.XPATH, "//li[contains(.,'Ihren Kunden')]"))
         WebDriverWait(self.driver, 5).until(element_present)
         self.driver.find_element_by_xpath("//li[contains(.,'Ihren Kunden')]").click()
         print("Selecting - Business Relation.......OK")

    # method to enable the newsletter option
    def enable_newsletter(self):
         print("Selecting - newsletter checkbox")
         element_present = EC.presence_of_element_located((By.XPATH, "//input[@name='newsletter']"))
         WebDriverWait(self.driver, 5).until(element_present)
         self.driver.find_element_by_xpath("//input[@name='newsletter']").click()
         print("newsletter checkbox is selected.......OK")

    # method to submit entered details
    # Additional for later: We can also use the double click event on button with Action Class
    def submit_details_on_signupPage(self):
        print("Submitting - details")
        element_present = EC.presence_of_element_located((By.XPATH, self.xpath_Button_signupPage))
        WebDriverWait(self.driver, 5).until(element_present)
        self.driver.find_element_by_xpath(self.xpath_Button_signupPage).click()
        print("Submitting - details.......OK")

    # method to get  and return the page details , return type: string
    def get_page_title(self):
        ActualTitle = self.driver.find_element_by_css_selector("h2.account__header__title").text
        return ActualTitle

    # method to verify the Phone number is missing validation message
    # We have created function to check the css type of the error message with its attribute type
    # once it is verified : we also verified the message text if its correct.
    # Note:
    # Scope: We can also verify if any other validation message
    # is also on the page or just single validation message is displayed

    def verify_errorMessage(self):
        print("Checking Error Message if present")
        css_locator_ErrorMessage_for_Phone = "p[id='name-error-text']"
        xpath_locator_ErrorMessage_for_Phone = "//p[text()='Dieses Feld ist ein Pflichtfeld']"
        element_present = EC.presence_of_element_located((By.XPATH, xpath_locator_ErrorMessage_for_Phone))
        WebDriverWait(self.driver, 5).until(element_present)
        print("Phone number validation message is present....OK.")
        print("Verifying Error Message if it is correct")

        ListErrorMessages = self.driver.find_elements_by_css_selector(css_locator_ErrorMessage_for_Phone)
        TotalMessageCount =  len(ListErrorMessages)
        print("------Total Validation Message Count:------->",TotalMessageCount )
        assert TotalMessageCount == 1
        print("Total Validation Message Count is .....OK")
        for i in range(len(ListErrorMessages)):
            attribute = ListErrorMessages[i].get_attribute("data-testid")
            print("Checking attribute")
            if attribute == "phone-error-message":
                print("attribute......is matched...OK")
                ErrorMessage = ListErrorMessages[i].text
                assert ErrorMessage == "Dieses Feld ist ein Pflichtfeld"
                print("Phone number is missing : validation message is matching")
                #if ErrorMessage == "Dieses Feld ist ein Pflichtfeld":
            else:
                continue
        print("Phone number is missing : validation message is displayed...OK")
