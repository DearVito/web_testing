import time
from selenium import webdriver
from math import log
from math import sin

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
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