#klasser och objekt

class nogger:
    def minklass(self):
        print("Mitt namn är: " + self.name)
        print("Mitt vikt är:" + self.vikt)


r1 = nogger()
r1.name = "Arvid"
r1.vikt = "67"

r2 = nogger()
r2.name = "Boliver"
r2.vikt = "80"

r1.minklass()
r2.minklass()



#Fråga 1
name = "Arvid"
#Fråga 2
age = 17
#Fråga 3
print("Hej, jag heter {name} och jag är {age} år gammal")