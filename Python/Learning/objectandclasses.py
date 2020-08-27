#Objekt och Klasser

#Gör klassen Robot

class Robot:
    def introduce_self(self):
        print("My name is " + self.name)

#
r1 = Robot()
r1.name = "Kazung"
r1.color = "Blue"
r1.weight = 70

#
r2 = Robot()
r2.name = "Boliver"
r2.color = "Pink"
r2.weight = 25

#Kör funktionen introuduce self
r1.introduce_self()
r2.introduce_self()