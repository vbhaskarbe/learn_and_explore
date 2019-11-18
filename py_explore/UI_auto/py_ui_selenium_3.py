from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def find_element( b_driver, attribute, a_value):
    #print('find_element: ', a_value)
    element = None
    if attribute == 'id':
        element = b_driver.find_element_by_id(a_value)
    elif attribute == 'link_text':
        element = b_driver.find_element_by_link_text(a_value)
    elif attribute == 'xpath':
        element = b_driver.find_element_by_xpath(a_value)
    else:
        print("find_element: UnHandled element type")
        exit(1)
    return element

def find_element_and_click( b_driver, attribute, a_value):
    element = find_element( b_driver, attribute, a_value)
    print("find_element_and_click: Clicking on the element:", a_value)
    element.click()

def start_browser( browser = 'Firefox'):
    if browser == 'Firefox':
        print("start_browser: browser type given is: ", browser)
        b_driver = webdriver.Firefox()
    else:
        print("start_browser: browser {} is not supported at this time".format(browser))
        exit(1)
    b_driver.get('https://www.seleniumeasy.com/test/')
    print( "Page Title: ", b_driver.title)
    return b_driver

def go_to_simple_form_demo( b_driver):
    print( "go_to_simple_form_demo: Page Title:", b_driver.title)
    find_element_and_click( b_driver, 'id', 'btn_basic_example')
    find_element_and_click( b_driver, 'link_text', 'Simple Form Demo')
    
def single_input_field( b_driver):
    print( 'single_input_field:', b_driver.title)
    ## Find the entry field
    element = find_element( b_driver, 'id', 'user-message')
    ## Type a message - Hello, UI-AUTOMATOR
    element.send_keys('Hello, UI-AUTOMATOR')
    ## Find and click on 'Show Message' button
    find_element_and_click( b_driver, 'xpath', "//button[text()='Show Message']")
    ## Find element and extract 'text' shown by it
    element = find_element( b_driver, 'xpath', "//span[@id='display']")
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

