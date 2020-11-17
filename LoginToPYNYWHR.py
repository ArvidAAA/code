from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from time import sleep
import random


USER = os.getenv('PYNYWHRUSR')
PASS = os.getenv('PYNYWHRPASS')

f = open("koder.txt", "a")

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://coke.studentkortet.se/')



firstsec = random.randint(2002,2003)
secondsec = random.randint(1, 12)
thirdsec = random.randint(1,25)
fourthsec = random.randint(1111, 9999)

if secondsec <= 9:
  secondsec="0" + str(secondsec)
else:
  secondsec=str(secondsec)

if thirdsec <= 9:
  thirdsec="0" + str(thirdsec)
else:
  thirdsec=str(thirdsec)

firstsec=str(firstsec)
secondsec=str(secondsec)
thirdsec=str(thirdsec)
fourthsec=str(fourthsec)

personaldank = firstsec + secondsec + thirdsec + fourthsec

print(personaldank)


usernameStr = personaldank
passwordStr = 'putYourPasswordHere'

username = driver.find_element_by_id('personal_number')
username.send_keys(usernameStr)
nextButton = driver.find_element_by_id('verify_button')
nextButton.click()



wait = WebDriverWait(driver, 10)

if wait.until(EC.url_changes('https://coke.studentkortet.se/')):
  print("Hämtar key, succesfully redirected")
  kod = driver.find_element_by_class_name('number')
  kod=str(kod.text)
  f.write(kod + "\n")
  driver.close()







print("Koden:")
print(kod)

## class = number
