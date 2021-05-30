from selenium import webdriver
import time
from math import log
from math import sin

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    button_troll = browser.find_element_by_css_selector('button.trollface')
    button_troll.click()
    
    new_browser = browser.window_handles[1]
    browser.switch_to.window(new_browser)
    x = browser.find_element_by_id('input_value').text
    x = int(x)
    y = str(log(abs(12*sin(x))))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    
    
finally:
    time.sleep(15)
    browser.quit()