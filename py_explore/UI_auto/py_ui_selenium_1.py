#
# Selenium script 
#   1. Open URL 'https://www.seleniumeasy.com/test' and click 'Start Practising'
#   2. On the new page, Click on Simple Form Demo
#   3. In the entry field shown, Type a message
#   4. Click on 'Show Message' button
#   5. Check if @ 'Your Message:' the text typed in '3' is shown.
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://www.seleniumeasy.com/test/')
print( browser.title)
browser.find_element_by_id('btn_basic_example').click()
print( browser.title)
browser.find_element_by_link_text('Simple Form Demo').click();
print( browser.title)
browser.find_element_by_id('user-message').send_keys('Hello, GURU')
browser.find_element_by_xpath("//button[text()='Show Message']").click()
element = browser.find_element_by_xpath("//span[@id='display']")
print( element.text)
browser.close()



