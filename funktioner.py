"""
Författare: Fredrik Stoltz
Datum: 
"""
from personMall import Person

import os


def huvudMeny():
    #“Skriver ut menyn etc, läser userinput för val. Ropar på lämplig funktion x vid val x.”
    print('''
    Vad vill du göra?

(1) Bläddra bland mina register
(2) Skapa ny kontakt
(3) Skapa nytt register
(4) Ändra/ta bort befintlig kontakt
''')
    val = int(input())
    if(val == 1):
        skrivUtRegister()
        pass
    elif(val == 2):
        skapaNyPerson()
    elif(val == 3):
        skapaNyttRegister()
        pass
    elif(val == 4):
        pass

def hamtaRegisterNamn():
    """filnamn = os.listdir("/home/fsto/Documents/Programmering och C/P-uppgift2019/")
    for name in filnamn:
        if(name[-3:] == "reg"):
            print"""
    file = open("register.info", "r")    
    
    lines = file.readlines()

    myDict = {}
    for i in range(0, len(lines)):
        myDict.update({i+1:lines[i]})
        #print("("+str(i+1)+") " + lines[i], end="")
        
    return(myDict)

def filNamnPaRadxIRegistret(x):
    pass


def skapaNyttRegister():
    namnPaRegister = input("Namn på nytt register: ")
    file = open("register.info", "a")
    file.write(namnPaRegister + "\n")

def skrivPersonTillRegister(person, registerNamn):
    file = open(registerNamn.lower() + ".reg", "a")
    file.write(person.skrivTillFil())

def laggTillPersonIRegister(nyKontakt):
    print("Till vilka register vill du lägga till nya kontakten?")
    namn = hamtaRegisterNamn()


    for value in namn.values():
        print(value)

    val = str(input(":"))
    if(len(val) == 1):
        #lägg till nyKontakt till det register som motsvarar valet
        skrivPersonTillRegister(nyKontakt, (namn.get(int(val)))[:-1]) # :-1 tar bort \n för filnamnet sedan i skrivPersonTillRegister
    else:
        nyttVal = val.split(",")
        print(nyttVal)


def skapaNyPerson():
    #Läser in userinput för värdena, låter anv. välja vilka register som personen ska tillhöra, skapar personen och lägger till den till lämpliga register.
    print("Du har valt att skapa en ny kontakt.")
    fornamn = input("Förnamn: ")
    efternamn = input("Efternamn: ")
    address = input("Address: ")
    telefonnummer = input("Telefonnummer: ")
    nyKontakt = Person(fornamn, efternamn, address, telefonnummer)
    laggTillPersonIRegister(nyKontakt)
    


def skrivAndringarTillRegisterFil(register):
    pass
    #Här skrivs nya ändringar till lämpligt register vid avslut av programmet

