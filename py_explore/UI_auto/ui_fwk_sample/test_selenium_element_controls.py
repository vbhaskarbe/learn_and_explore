
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_selenium_utilities  import TestSeleniumUtilities
import time

class TestSeleniumElementControls( TestSeleniumUtilities):
    def __init__( self, element_class, ui_driver):
        self.b_driver =  ui_driver
        
    def find_element( self, attr_type, attr_value):
        self.element = None
        try:
            find_function = getattr( self.b_driver, 'find_element_by_' + attr_type)
            self.element = find_function(attr_value)
        except Exception as e:
            print("Error: ", e)
            exit(1)
        return self.element
 
    def find_element_and_click( self, attr_type, attr_value):
        self.find_element( attr_type, attr_value).click()
        self.uiCommonUtils.take_screenshot( self.b_driver)

if __name__ == '__main__':
    from test_selenium_elements import TestSeleniumElements
    from test_selenium_base import TestSeleniumBase
    ts_base           = TestSeleniumBase( )
    ts_el_ctrl_object = TestSeleniumElementControls( TestSeleniumElements)

        

