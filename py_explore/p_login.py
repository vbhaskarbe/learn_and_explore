########################################################################
##  prezent.ai UI Automation By Bhaskar V.
## :: ToDo ::
##  (1) Environment Variables 
##  (2) Property file variables (config) 
##  (3) Browser specific settings - Download loc? etc
##  (4) Screenshots and convert to PDF
##  (5) Pytest integration
##  (6) Page object for Login page
##  (7) Logger integration
##  (8) Testsuite file with @ui_init decorator
##  (9) Running in docker (all browsers)
## (10)  
## 
########################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 

class PySelenium_UI_Practice():
    #test_site = os.get.environ('TEST_PRODHOST', 'https://teams.prezent.ai/')
    test_site = 'https://teams.prezent.ai/'
    def __init__( self, browser = 'Firefox', prod_site = test_site):
        self.browser   = browser
        self.b_driver  = None
        self.prod_site = prod_site

    def find_elements( self, attr_type, attr_value):
        self.element = None
        try:
            find_function = getattr( self.b_driver, 'find_elements_by_' + attr_type)
            self.elements = find_function(attr_value)
        except Exception as e:
            print("Error: ", e)
            exit(1)
        return self.elements

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
        elif self.browser == 'Chrome':
            self.b_driver = webdriver.Chrome()
        elif self.browser == 'Safari':
            self.b_driver = webdriver.Safari()
        elif self.browser == 'Edge':
            desired_cap   = {}
            self.b_driver = webdriver.Edge(executable_path='/Users/bhasvara/ztmp/msedgedriver', capabilities=desired_cap)
        else:
            print("start_browser: browser {} is not yet supported".format(self.browser))
            exit(1)
        self.b_driver.maximize_window()
        print("start_browser: Go to the demo site:", self.prod_site)
        self.b_driver.get(self.prod_site)

    def do_login( self):
        self.find_element('id', 'username').click()
        print("######## ######## ######## ########")
        uelement = self.find_element('id', 'username')
        uelement.send_keys(os.environ['TEST_USERNAME'])
        ## eye off - Type is password, Eye on - Type is text
        pelement = self.find_element('id',"password")
        pelement.send_keys(os.environ['TEST_PASSWORD'])
        time.sleep(2)
        self.find_element('id',"submit").click()
        img_element = WebDriverWait(self.b_driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//img[contains(@src,'profile.svg')]")))
        print(img_element)
        #print(dir(img_element))
        
    def close_browser( self):
        print("close_browser: *** All done! Time to close the browser ***")
        self.b_driver.close()

if __name__ == '__main__':
    #selui_object = PySelenium_UI_Practice()
    test_browser  = os.environ.get('TEST_BROWSER', 'Firefox')
    test_prodhost = os.environ['TEST_PRODHOST']
    selui_object  = PySelenium_UI_Practice(test_browser, test_prodhost)

    selui_object.do_login()
    
    selui_object.close_browser()

