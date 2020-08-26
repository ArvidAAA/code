#Skriva och läsa text dokument

#Print
print("Skriva och Läsa .txt filer")


#Öppnar textfilen i bakgrunden
file = open("testfil.txt", "w+")
#Skriver Hello
file.write("Hello")
#Stäng filen
file.close()


#läsa av textfilen och printa
file = open("testfil.txt", "r")
print(file.read())

