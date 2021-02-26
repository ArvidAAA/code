#Musik i python test
#2020 24 NOV
from playsound import playsound


#Definerar funktionen
def ljud():
    #Variabel med innehållet av min ljudfil som ligger i samma mapp och heter ljudtest.mp3
    minljudfil = "ljudtest.mp3"
    #Använder playsound modulen för att spela upp filen
    playsound(minljudfil)

#Kör funktionen
ljud()

