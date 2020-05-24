from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class PySelenium_UI():
    test_site = 'https://www.seleniumeasy.com/test/'
    def __init__( self, browser = 'Firefox', demo_site = test_site):
        self.browser   = browser
        self.b_driver  = None
        self.demo_site = demo_site
        self.counter   = 1
        self.testname  = 'py_selenium_case'
    
    ## Take screenshots to help with debug later.
    def take_screenshot( self):
        self.b_driver.save_screenshot( self.testname + '_' + str(self.counter).zfill(3) + '.PNG')
        self.counter = self.counter + 1
    
    def process_screenshots( self):
        import glob
        from zipfile import ZipFile
        try:
            png_files_list = glob.glob( os.path.join( self.testname + '_*.PNG'))
            with ZipFile( self.testname + '.zip', 'w') as zipObj:
                for filename in png_files_list:
                    zipObj.write( filename, os.path.basename(filename))
                    os.remove( filename)
            zipObj.close()
        except Exception as e:
            print("process_screenshots: Failed: %s" % str(e))
        finally:
            print( "Screenshots are zipped up in to %s" % (self.testname + '.zip'))

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
        else:
            print("start_browser: browser {} is not yet supported".format(self.browser))
            exit(1)
        print("start_browser: Go to the demo site:", self.demo_site)
        self.b_driver.get(self.demo_site)
        self.take_screenshot()
        self.find_element_and_click( 'id', 'at-cv-lightbox-close')
        self.take_screenshot()

    def go_to_simple_form_demo( self):
        print( "go_to_simple_form_demo:", self.b_driver.title)
        self.find_element_and_click( 'id', 'btn_basic_example')
        self.take_screenshot()
        self.find_element_and_click( 'link_text', 'Simple Form Demo')
        self.take_screenshot()

    def single_input_field_test( self):
        print( 'single_input_field_test: Find single entry field and type a value')
        ## Find the entry field and type - 'Hello, UI-AUTOMATOR' text
        self.find_element( 'id', 'user-message').send_keys('Hello, UI-AUTOMATOR')
        self.take_screenshot()
        ## Find and click on 'Show Message' button
        self.find_element_and_click( 'xpath', "//button[text()='Show Message']")
        self.take_screenshot()
        ## Find element and extract 'text' shown by it
        element = self.find_element( 'xpath', "//span[@id='display']")
        print( "Text entered is :", element.text)

    def close_browser( self):
        print("close_browser: *** All done! Time to close the browser ***")
        self.take_screenshot()
        self.b_driver.close()
        self.process_screenshots()

if __name__ == '__main__':
    selui_object = PySelenium_UI()
    selui_object.start_browser()
    selui_object.go_to_simple_form_demo()
    selui_object.single_input_field_test()
    selui_object.close_browser()

