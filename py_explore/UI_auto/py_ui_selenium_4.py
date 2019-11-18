from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SelUI_Practice():
    def __init__( self, browser = 'Firefox'):
        self.browser   = browser
        self.b_driver  = None
        self.demo_site = 'https://www.seleniumeasy.com/test/'

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
        self.element = self.find_element( attr_type, attr_value)
        self.element.click()
        time.sleep(1)

    def start_browser( self):
        if self.browser == 'Firefox':
            self.b_driver = webdriver.Firefox()
        else:
            print("start_browser: browser {} is not yet supported".format(self.browser))
            exit(1)
        self.b_driver.get(self.demo_site)
        print( self.b_driver.title)

    def go_to_simple_form_demo( self):
        print( "go_to_simple_form_demo:", self.b_driver.title)
        self.find_element_and_click( 'id', 'btn_basic_example')
        self.find_element_and_click( 'link_text', 'Simple Form Demo')

    def single_input_field_test( self):
        print( 'single_input_field_test:', self.b_driver.title)
        ## Find the entry field
        element = self.find_element( 'id', 'user-message')
        ## Type a message - Hello, UI-AUTOMATOR
        element.send_keys('Hello, UI-AUTOMATOR')
        ## Find and click on 'Show Message' button
        self.find_element_and_click( 'xpath', "//button[text()='Show Message']")
        ## Find element and extract 'text' shown by it
        element = self.find_element( 'xpath', "//span[@id='display']")
        print( "Text entered is :", element.text)

    def close_browser( self):
        print("close_browser: All done! Time to close the browser")
        self.b_driver.close()

if __name__ == '__main__':
    selui_object = SelUI_Practice()
    selui_object.start_browser()
    selui_object.go_to_simple_form_demo()
    selui_object.single_input_field_test()
    selui_object.close_browser()

