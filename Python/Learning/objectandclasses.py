#Objekt och Klasser

#Gör klassen Robot

from os import system
from os import name


if name == 'nt':
    system('cls')
else:
        system('clear')


spar1 = open("objectsparfil.txt", "+w")

class Robot:
    def introduce_self(self):
        return("My name is " + self.name)

r1 = Robot()
r1.name = "Kazung"
r1.color = "Blue"
r1.weight = 70


#
r2 = Robot()
r2.name = "lol"
r2.color = "Pink"
r2.weight = 25


#Kör funktionen introuduce self
spar1.write(r1.introduce_self())
spar1.write("\n")
spar1.write(r2.introduce_self())


