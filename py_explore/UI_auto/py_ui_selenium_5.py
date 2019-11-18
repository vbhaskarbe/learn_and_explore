from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PySelenium_UI_Practice():
    test_site = 'https://www.seleniumeasy.com/test/'
    def __init__( self, browser = 'Firefox', demo_site = test_site):
        self.browser   = browser
        self.b_driver  = None
        self.demo_site = demo_site

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

    def start_browser( self):
        print("start_browser: start the browser:", self.browser)
        if self.browser == 'Firefox':
            self.b_driver = webdriver.Firefox()
            self.b_driver.maximize_window()
        else:
            print("start_browser: browser {} is not yet supported".format(self.browser))
            exit(1)
        print("start_browser: Go to the demo site:", self.demo_site)
        self.b_driver.get(self.demo_site)

    def go_to_required_form( self, formname = 'Simple Form Demo'):
        self.find_element('link_text', 'Demo Home').click()
        print( "go_to_required_form:", formname)
        self.find_element_and_click( 'id', 'btn_basic_example')
        self.find_element_and_click( 'link_text', formname)

    def single_input_field_test( self):
        print( 'single_input_field_test: Find single entry field and type a value')
        ## Find the entry field
        element = self.find_element( 'id', 'user-message')
        ## Type a message - Hello, UI-AUTOMATOR
        element.send_keys('Hello, UI-AUTOMATOR')
        ## Find and click on 'Show Message' button
        self.find_element_and_click( 'xpath', "//button[text()='Show Message']")
        ## Find element and extract 'text' shown by it
        element = self.find_element( 'xpath', "//span[@id='display']")
        print( "Text entered is :", element.text)

    def two_input_fields_test(self):
        self.find_element( 'id', 'sum1').send_keys('10')
        self.find_element( 'id', 'sum2').send_keys('20')
        self.find_element_and_click( 'xpath', "//button[text()='Get Total']")
        time.sleep(2)
        print("Sum of 10 + 20 is:", self.find_element( 'xpath', "//span[@id='displayvalue']").text)

    def single_checkbox_demo(self):
        element = self.find_element('id', 'isAgeSelected')
        if element and (not element.is_selected()):
            print("The check box is not yet selected")
            element.click()
        element = self.find_element('xpath', "//div[@id='txtAge']")
        print("Message after click() on check box is: ", element.text)

    def multiple_checkbox_demo(self):
        pass

    def close_browser( self):
        print("close_browser: *** All done! Time to close the browser ***")
        self.b_driver.close()

if __name__ == '__main__':
    selui_object = PySelenium_UI_Practice()
    selui_object.start_browser()
    selui_object.go_to_required_form()
    selui_object.single_input_field_test()
    selui_object.two_input_fields_test()
    
    selui_object.go_to_required_form('Check Box Demo')
    selui_object.single_checkbox_demo()
    selui_object.multiple_checkbox_demo()
    
    selui_object.close_browser()

