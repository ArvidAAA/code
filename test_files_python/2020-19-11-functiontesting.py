#2020-19-11
#Testar lite python


#Test 1
arginput1 = int(input("Mata in din första interger "))
arginput2 = int(input("Mata in din andra interger "))

def minfunktion1(arg1, arg2):
    return(arg1 * arg2)

print(minfunktion1(arginput1,arginput2))


#Går att använda pass om du vill ha en tom funktion men undvika error
def passing():
    pass
print("Hej")



#Printar en lista med hjälp av en funktion, (onödigt)
def dankster(minfinalista):
    print(minfinalista)

beverge = ["Bärs", "Sprit", "Vin"]

dankster(beverge)


#Kör igenom listan och printar ut allt i listan på olika rader
def dankster1(minfinalista1):
    for dankero in minfinalista1:
        print(dankero)

beverge1 = ["Bärs", "Sprit", "Vin", "Saft"]
dankster1(beverge1)

#Printar var man kommer ifrån för land, rad för rad
def printmycountry(mittland):
    print(f"I am from {mittland}")

printmycountry("Sweden")
printmycountry("Russia")
printmycountry("Belarus")