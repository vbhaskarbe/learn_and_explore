############################################################################
## Author: Bhaskar Varadaraju
##  A Program to demonstrate multi-browser support with selenium
##  Prereqs: Python3, selenium, Firefox (geckodriver), Chrome(chromedriver),
##           Edge (msedgedriver), and Safari
## 
##  Usage  : export TEST_BROWSER=<Firefox|Chrome|Safari|Edge>
##           python3 sel_browser_demo.py
## 
############################################################################
from selenium import webdriver
import os 

class PySelenium_UI_Practice():
    test_site = 'https://www.seleniumeasy.com/'
    def __init__( self, browser = 'Firefox', prod_site = test_site):
        self.browser   = browser
        self.b_driver  = None
        self.prod_site = prod_site

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
            self.b_driver = webdriver.Edge(executable_path='/home/ubuntu/msedgedriver', capabilities=desired_cap)
        else:
            print("start_browser: browser {} is not yet supported".format(self.browser))
            exit(1)
        self.b_driver.maximize_window()
        print("start_browser: Go to the test site:", self.prod_site)
        self.b_driver.get(self.prod_site)

    def close_browser( self):
        print("close_browser: *** All done! Time to close the browser ***")
        self.b_driver.close()

if __name__ == '__main__':
    test_browser  = os.environ.get('TEST_BROWSER', 'Firefox')
    selui_object  = PySelenium_UI_Practice(test_browser)
    selui_object.start_browser()
    selui_object.close_browser()

