from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import inspect

from test_selenium_elements import TestSeleniumElements
from test_selenium_base import TestSeleniumBase

class TestSeleniumService( TestSeleniumBase):

    def __init__( self, ui_driver):
        self.ui_driver    = ui_driver
        self.ui_driver.implicitly_wait(180)
        self.ts_elements  = TestSeleniumElements( self.ui_driver)

    def close_popup( self):
        print( "close_popup:", self.ui_driver.title)
        self.el_close_popup.click()

    def go_to_simple_form_demo( self):
        print( "go_to_simple_form_demo:", self.ui_driver.title)
        self.el_basic_example.click()
        self.el_simple_form_demo.click()

    def single_input_field_test( self, user_text):
        print( 'single_input_field_test: Find single entry field and type a value')
        ## Find the entry field and type - 'Hello, UI-AUTOMATOR' text
        self.el_si_user_message.send_keys( user_text)
        ## Find and click on 'Show Message' button
        self.el_si_show_message.click()
        ## Find element and extract 'text' shown by it
        print( "Text entered is :", self.el_si_display.text)
        return self.el_si_display.text 

    def __getattr__(self, el_name):
        return self.ts_elements.get_element( el_name)

if __name__ == '__main__':

    selbase_obj  = TestSeleniumBase()
    selbase_obj.start_browser()
 
    selui_object = TestSeleniumService( selbase_obj.b_driver)

    try:
        import time
        time.sleep(2)
        selui_object.close_popup()
        selui_object.go_to_simple_form_demo()
        selui_object.single_input_field_test("Hello! Bhaskar")
    finally:
        selbase_obj.close_browser()

