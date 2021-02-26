#Rensa skären/terminalen


#Behövs importera system och name från OS
from os import system, name

#funktion vid namn clear
def clear():
    # name = os version, nt står för windows / posix står för mac/linux
    if name == 'nt':
        #cls rensar skärmen i windows
        system('cls')
    else:
        #clear rensar skärmen i mac/linux
        system('clear')


#Testar rensa skärmen

print("Spam")
print("Spam")
print("Spam")
print("Spam")
print("Spam")
clear()