#COCA COLA BOT CHROMEDRIVER BY ARVID for educational purposes only
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from time import sleep
import random


print("COCA COLA BOT CHROMEDRIVER BY ARVID for educational purposes only")
sleep(1)


#Funktionen bot
def bot():
  f = open("koder.txt", "a")

  driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
  driver.get('https://coke.studentkortet.se/')


  #Personnummer generator i rätt årsspann
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

  #Usernamestr = personnummret
  usernameStr = personaldank

  #Fält för personnummret
  username = driver.find_element_by_id('personal_number')
  username.send_keys(usernameStr)
  #Knapp
  nextButton = driver.find_element_by_id('verify_button')
  nextButton.click()


  sleep(3)
  #While loop
  while True:
          try:
            if driver.find_element_by_class_name('number'):
              kod = driver.find_element_by_class_name('number')
              kod=str(kod.text)
              f.write(kod + "\n")
              print("Koden:")
              print(kod)
              f.close()
              driver.close()
              bot()
          except:
              f.close()
              driver.close()
              bot()


#Används för att starta botten när du kör programmet direkt
bot()