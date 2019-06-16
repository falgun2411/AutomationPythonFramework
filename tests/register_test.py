import time
import pytest
from pages.homePage import HomePage
from pages.leasingPage import LeasingPage
from pages.searchPage import SearchPage
from pages.signupPage import SignUpPage
from utils import utils as utils


# Note: We also use timeout Options  + WebdriverWait both to make sure Test case does not fail,
# Reason: Sometimes selenium is too fast that even though field is there it is not recognizing due to fast process
# Ideally we should minimize the use of timeout but here it was not working with WebdriverWait so we use timeout
# I also observed we can use the element locator css selector for this , in later Phase
# Css selector will be good option for IE Browser
# Note: there is possibility that some locators are
# keep changing we need to check and make a note for it for such element type

@pytest.mark.usefixtures("test_setup")
# it by default checks the "conftest.py" file to get the test_setup

class TestRegistration():

    # TestCase Summary: To Select the category from the Main Page
    # Steps:
    # 1. Launch Browser and Go to base URL
    # 2. Object is created for HomePage
    # 3. Get the HomePage title and verify if its correct page
    # 4. Click on the category : Leasing & Mietkauf
    # User will be redirected to new page: LeasingPage
    # 5. Object is created for leasingPage
    # 6. Get the LeasingPage title and verify user is landed on correct page

    def test_firstPage(self):
            driver = self.driver
            driver.get(utils.URL)
            TitleName = utils.TitleName_Leasing
            homePageAction = HomePage(driver)
            ActualTitle = homePageAction.get_page_title()
            ExpectedTitle = "Welche Finanzierungslösung suchen Sie?"
            assert ActualTitle == ExpectedTitle

            homePageAction.select_title(TitleName)
            time.sleep(5)

            leasingPageAction = LeasingPage(driver)
            ActualTitle = leasingPageAction.get_page_title()
            ExpectedTitle = "Finden Sie die besten Leasing - oder Mietkaufangebote"
            assert ActualTitle == ExpectedTitle

    # TestCase Summary: To Enter correct Category details and click on submit button
    # Steps:
    # 1. User is redirected on Leasing Category Page
    # 2. Object is created for leasingPage
    # 3. Get the LeasingPage title and verify user is landed on correct page
    # from this object call method from the Leasing Page and perform
    # 4. Enter details for Amount
    # 5. Enter details form drop down option of Category
    # 6. Enter details form drop down option of Sub Category
    # 7. Scroll down to window page, to visible other options
    # 8. Enter details form drop down option of Term
    # 9. Submit the filled details by clicking submit button
    # User will be redirected to new page: searchPage
    # 10. Object is created for searchPage
    # 11. Get the SearchPage title and verify user is landed on correct page
    # Note: We also use timeout Options  + WebdriverWait both to make sure Test case does not fail,
    # Reason: Sometimes selenium is too fast that even though field is there it is not recognizing due to fast process
    # Ideally we should minimize the use of timeout but here it was not working with WebdriverWait so we use timeout

    def test_SecondPage(self):
            driver = self.driver
            leasingPageAction = LeasingPage(driver)
            ActualTitle = leasingPageAction.get_page_title()
            ExpectedTitle = "Finden Sie die besten Leasing - oder Mietkaufangebote"
            assert ActualTitle == ExpectedTitle

            leasingPageAction.enter_amount()
            time.sleep(3)
            leasingPageAction.enter_AssetCategory()
            time.sleep(3)
            leasingPageAction.enter_AssetType()
            time.sleep(4)
            driver.execute_script("window.scrollTo(0, 1000);")
            time.sleep(3)
            leasingPageAction.enter_AssetTerm()
            time.sleep(3)
            leasingPageAction.submit_details()
            time.sleep(10)

            searchPageAction = SearchPage(driver)
            ActualTitle = searchPageAction.get_page_title()
            ExpectedTitle = "Für welches Unternehmen benötigen Sie die Finanzierung?"
            assert ActualTitle == ExpectedTitle

    # TestCase Summary: To Enter correct Category details and click on submit button
    # Steps:
    # 1. User is redirected on searchPage
    # 2. Object is created for searchPage
    # 3. Get the SearchPage title and verify user is landed on correct page
    # from this object call methods from the Search Page and perform
    # 4. Enter details for Company Name
    # 5. Submit the filled details by SUBMIT Option
    # 6. Select the company name from the search results
    # User will be redirected to new page: registrationPage
    # 7. Object is created for registrationPage
    # 8. Get the registrationPage title and verify user is landed on correct page

    def test_ThirdPage(self):
            driver = self.driver
            searchPageAction = SearchPage(driver)
            ActualTitle = searchPageAction.get_page_title()
            ExpectedTitle = "Für welches Unternehmen benötigen Sie die Finanzierung?"
            assert ActualTitle == ExpectedTitle

            Seach_CompanyName = utils.Search_keyword_for_comapnyName
            searchPageAction.enter_companyName(Seach_CompanyName)
            searchPageAction.submit_the_companyName()
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 1000);")
            time.sleep(3)
            searchPageAction.select_comapny_from_searchresult(Seach_CompanyName)
            time.sleep(5)

            signupPageAction = SignUpPage(driver)
            ActualTitle = signupPageAction.get_page_title()
            ExpectedTitle = "Registrierung"
            assert ActualTitle == ExpectedTitle

    # TestCase Summary: To Enter correct Category details and click on submit button
    # Steps:
    # 1. User is redirected on Registration Page
    # 2. Object is created for Registration Page
    # 3. Get the Registration Page title and verify user is landed on correct page
    # from this object call method from the Registration Page and perform
    # 4. Enter details for FirstName
    # 5. Enter details for LastName
    # 6. Enter details for EMail
    # 7. Enter details form drop down option of Business relation
    # 8. Scroll down to window page, to visible other options
    # 9. Enter details form CheckBox : newsletter
    # 10. Make Sure: We did not fill the Phone number field
    # Result:
    # User will remain on same page, Phone Number field validation message will displayed
    # 11. Now, Verify this message is correct and also its attribute type
    # 12. Get the registration title and verify user is landed on correct page

    def test_FourthPage(self):
            driver = self.driver

            signupPageAction = SignUpPage(driver)
            time.sleep(5)
            ActualTitle = signupPageAction.get_page_title()
            ExpectedTitle = "Registrierung"
            assert ActualTitle == ExpectedTitle

            signupPageAction.enter_firstname(utils.FIRSTNAME)
            signupPageAction.enter_lastname(utils.LASTNAME)
            signupPageAction.enter_email(utils.EMAIL)
            time.sleep(3)
            signupPageAction.enter_buisnessrelation()
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 1000);")
            time.sleep(3)
            signupPageAction.enable_newsletter()
            time.sleep(3)
            signupPageAction.submit_details_on_signupPage()
            time.sleep(5)
            signupPageAction.verify_errorMessage()
            time.sleep(10)

            ActualTitle = signupPageAction.get_page_title()
            assert ActualTitle == ExpectedTitle