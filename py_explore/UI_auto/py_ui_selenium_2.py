from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#
## Prereqs: Firefox browser, Python3, Selenium, Geckodriver, Internet?
#

def start_browser( browser = 'Firefox'):
    if browser == 'Firefox':
        print("start_browser: browser type given is: ", browser)
        b_driver = webdriver.Firefox()
    else:
        print("start_browser: browser {} is not supported at this time".format(browser))
        exit(1)
    b_driver.get('https://www.seleniumeasy.com/test/')
    print( b_driver.title)
    return b_driver

def go_to_simple_form_demo( b_driver):
    print( "go_to_simple_form_demo:", b_driver.title)
    b_driver.find_element_by_id('btn_basic_example').click()
    print( b_driver.title)
    b_driver.find_element_by_link_text('Simple Form Demo').click();
    
def single_input_field( b_driver):
    print( 'single_input_field:', b_driver.title)
    b_driver.find_element_by_id('user-message').send_keys('Hello, GURU')
    time.sleep(2)
    b_driver.find_element_by_id('at-cv-lightbox-close').click()
    time.sleep(1)
    b_driver.find_element_by_xpath("//button[text()='Show Message']").click()
    time.sleep(2)
    element = b_driver.find_element_by_xpath("//span[@id='display']")
    print( "Text entered is :", element.text)

def close_browser( b_driver):
    print("close_browser: All done! Time to close the browser")
    b_driver.close()

if __name__ == '__main__':
    #b_driver = start_browser('Chrome')
    b_driver = start_browser()
    go_to_simple_form_demo( b_driver)
    single_input_field( b_driver)
    close_browser( b_driver)

