# This is Main category Page, showing options to user to select any category


class HomePage():

    def __init__(self, driver):
        # xapth used for this page
        self.driver = driver
        self.xpath_Leasing_Title = "//h2[text()='Leasing & Mietkauf']"
        self.css_Leasing_Title = "//h2[text()='Leasing & Mietkauf']"
        self.xpath_Kredit_Title = "//h2[text()='Kredit']"
        self.xpath_Factoring_Title = "//h2[text()='Factoring']"
        value = "h2.funnel__products__title:contains(Leasing & Mietkauf)"
        self.Select_Title_Leasing = "Leasing & Mietkauf"
        self.Select_Title_Kredit = "Kredit"

    # Method: to Select leasing title directly
    def click_xpath_LeasingPage(self, xpath_Leasing_Title):
        self.driver.find_element_by_xpath(self.xpath_Leasing_Title).click()

    # method to get  and return the page details , return type: string
    def get_page_title(self):
        ActualTitle = self.driver.find_element_by_css_selector("h1.funnel__products__heading").text
        return ActualTitle

    # Method: to Select leasing title from the List of options on Main page
    # Later Scope ACHIEVED: A dynamic method will be needed to check all drop down options and click from that option
    # Input Type: String (CategotyName) , results: CategoryName is clicked
    def select_title(self, Select_Title_Leasing):
        TitleTobeClicked = Select_Title_Leasing
        CategoryList = self.driver.find_elements_by_css_selector("h2.funnel__products__title")

        for i in range(len(CategoryList)):
            CategoryName = CategoryList[i].text
            print("Verifying the module name:- "+ CategoryName)
            if CategoryName == TitleTobeClicked:
                break
        CategoryList[i].click()
        print(CategoryName + "......is clicked")




