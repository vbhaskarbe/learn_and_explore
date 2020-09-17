
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_selenium_configuration import TestSeleniumConfiguration

import time

class TestSeleniumBase():
    def __init__( self):
        tb_properties = TestSeleniumConfiguration().getDefault()
        self.browser  = tb_properties.BROWSER
        self.b_driver = None
        self.site_url = tb_properties.SITE_URL

    def start_browser( self):
        print("start_browser: start the browser:", self.browser)
        if self.browser == 'Firefox':
            self.b_driver = webdriver.Firefox()
        else:
            print("start_browser: browser {} is not yet supported".format(self.browser))
            exit(1)
        print("start_browser: Go to the demo site:", self.site_url)
        self.b_driver.get(self.site_url)

    def close_browser( self):
        print("close_browser: *** All done! Time to close the browser ***")
        self.b_driver.close()

    def find_element_2( self, element, ui_driver, attr_type, attr_value):
        self.element = None
        try:
            find_function = getattr( ui_driver, 'find_element_by_' + attr_type)
            setattr( self, element, find_function(attr_value))
        except Exception as e:
            print("Error: ", e)
            exit(1)
#        return self.element
    
if __name__ == '__main__':
    from test_selenium_configuration_dto import TestSeleniumConfigurationDTO
    selui_object = TestSeleniumBase()
    selui_object.start_browser()
    selui_object.close_browser()

