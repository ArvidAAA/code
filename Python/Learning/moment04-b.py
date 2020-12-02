#moment04-b


def uppgift1():
    ########################################
    print("Inlämmningsuppgift moment04 a")
    print("Enheter i cm3")
    ########################################
    #Skapat dessa för att inte Visual Studio Code ska jobba sig
    s1 = 0
    s2 = 0
    #Input för heltal 1 och 2
    s1 = int(input("Ange basen på rektangeln: "))
    s2 = int(input("Ange höjden på rektangeln: "))
    

    #Area = b * h
    area = s1 * s2
    #Printar ut arean
    print(f"Arean på rektangeln är {area}")

    if s1 == s2:
        print(f"Rektangeln har sidorna {s1} och {s2} detta betyder att det är en kvadrat eftersom sidorna är lika långa")
    else:
        print(f"Rektangeln har sidorna {s1} och  {s2}")
    

