#Göra en lista

minlista = ["Apple", "Banana", "Pear", "Watermelon"]


#Printa listan

print(minlista)


#Välja en specefik grej från listan att printa. Börjar alltid från 0 så i detta fallet är Apple 0.
#Du kan också gå igenom listan baklänges med te.x -1 -2 -3
print(minlista[0])


#Vill du få ut alla mellan te.x Banan och Watermelon. 
# I detta fallet är 0:an med medans 2:an ej är med
print(minlista[0:3])


#Du kan också börja och starta på olika ställen
print(minlista[:3])
print(minlista[2:])


#Byta ut grejer i listan. Detta byter ut Banana mot BlackPear
minlista[1] = "BlackPear"
print(minlista)

minlista.append = ("Hello")