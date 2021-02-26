from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


usernameStr = 'yourafuckingscammer'
passwordStr = 'stopwithwhatyouaredoing'

browser = webdriver.Chrome()
browser.get(('https://uwikkontolbenerbenerkontol.feathercapitalpartners.com/r/RqsSb8j'))




username = browser.find_element_by_id('email')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('btnNext')
nextButton.click()

time.sleep(5)

username = browser.find_element_by_id('password')
username.send_keys(passwordStr)
signInButton = browser.find_element_by_id('btnNext')
signInButton.click()