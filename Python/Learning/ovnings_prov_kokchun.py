# Övningsprov Kokchun, arvid
import random as rnd

def uppgift_1():
    birds = 8000
    year = 0
    while birds > 800:
        year += 1
        birds /= 2
        print(f"˚Ar {year}: antal fåaglar: {birds:.0f}")


""" Medans fåglarna är mer än 800 så fortsätter 
while loopen och den lägger till ett år och halverar antalet fåglar samt printar ut för varje gång loopen hur många fåglar som finns kvar varje år och fåglar"""


# uppgift_1()

def uppgift_2():
    pass


def uppgift_3(a, b, c):
    medelvärde = (a + b + c) / 3
    print(medelvärde)


# uppgift_3(1,3,5)


def uppgift_4(r):
    volym = (4 * 3.14 * r ** 3) / 3
    print(volym)


# uppgift_4_userinput = float(input("Mata in din radie: "))
# uppgift_4(uppgift_4_userinput)

def uppgift_5():
    mening = str(input("Mata in din mening: "))
    print("Antal ord i meningen:", len(mening.split(" ")))


# uppgift_5()


def uppgift_6():
    while True:
        fel = 0
        try:
            user_input = int(input("Mata in det heltalet du vill öva på: "))
        except:
            print("Det var inget heltal")
        for i in range(1, 11):
            while True:
                for_input = int(input(f'Vad blir {user_input} * {i} blir: '))
                if user_input * i != for_input:
                    print("WRONG")
                    fel += 1
                else:
                    print("RIGHT")
                    break
        print(" ")
        print("Bra jobbat!")
        print(f'Du hade {fel} fel')
#uppgift_6()

def uppgift_7():
    antal_femmor = 0
    for i in range(1, 10001):
        tärning = rnd.randint(1, 6)
        if tärning == 5:
            antal_femmor += 1
        else:
            pass
    print(antal_femmor)

#uppgift_7()


def uppgift_8(summa):
    kontanter = [1000, 500, 200, 100, 50, 20, 10, 5, 1]  # sedlar o mynt
    sedlar = ["tusenlappar", "femhundralappar", "tvåhundralappar", "hundralappar", "femtiolappar", "tjugolappar",
              "tiokronor", "femkronor", "enkronor"]

    for i in range(len(kontanter)):
        antal = summa // kontanter[i]  # heltalsdivision
        summa %= kontanter[i]  # ger resten vid heltalsdivision per sedel
        print(f"{antal} {sedlar[i]}", end=", ")  # skriver ut antal per sedel

#uppgift_8(3899)


def uppgift_9():
    #

def uppgift_10():
    #Blackjack most important pop, shuffle from random