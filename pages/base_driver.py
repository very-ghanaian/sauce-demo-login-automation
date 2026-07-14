class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    #We have an update in method why we took the "id" out of the find method and put it in the base_driver.py file. So we can use it in other pages as well.
    def find(self, by, locator_value):
        return self.driver.find_element(by, locator_value)

    #this method is for finding elements by different locators like name, class, xpath, etc. We can use it in other pages as well.
    ##def find(self, by, locator_value):
    ######return self.driver.find_element(by, locator_value)