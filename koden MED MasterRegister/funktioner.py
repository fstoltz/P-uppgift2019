"""
Författare: Fredrik Stoltz
Datum: 29/10-2019
"""
from personMall import Person
from registerMall import Register
from MasterRegisterMall import MasterRegister
import sys
"""
ATT GÖRA:

(
Felhantering.
Try except för input, Öppnande av filer(filer som ej finns etc, svenska bokstäver(?)), skapande av register som redan finns.
Rensa input från dålig data. Mellan slag etc. Tecken där det bara ska vara siffror etc. Bra felhantering. Programmet ska ej krascha.
Kunna använda svenska å,ä,å för registernamn?? konvertera för filnamn??
)

(
Sök funktionalitet. / Sök på valda registren
)

(
Ta bort/Ändra funktionalitet.
)
"""

def huvudMeny(firstTime=1, master=None):
    #“Skriver ut menyn etc, läser userinput för val. Ropar på lämplig funktion x vid val x.”
    
    #master.skrivUtRegister()

    
    if(firstTime == 1):
        print("----->  Ange '!' för att närsomhelst komma tillbaka till huvudmenyn.")
        master = MasterRegister()
        master.skapaRegisterMedRespNamn()
        master.laddaAllaRegisterMedInfoFranFil()

    while(1):
        huvudMenyInstruktioner()
        
        val = readInput(master, "Svar: ")
    
        if(val == '1'):
            try:
                master.skrivUtRegister()
                valen = master.valjRegister(readInput(master, "\nVilka register vill du söka inom?\nEx. ange '3' för register nr.3 alt. '3,5,1' för register tre, fem och ett(samkörning).\n"))
                
                print("Ange ENTER för att söka utan någon term, dvs alla kontakter skrivs ut.")
                keyword = readInput(master, "Sökterm: ")
            
                master.sok("LETA", keyword, valen)
            except:
                print("Something went wrong...")
            
        

        elif(val == '2'):
            skapaNyPerson(master)
        

        elif(val == '3'):
            master.skapaNyttRegister(readInput(master, "Namn på nya registret: "))
        

        elif(val == '4'):
            userinput1 = readInput(master, "Vill du ändra(1) eller ta bort personen(2)?")
            if(userinput1 == "2"):
                #print("#attempt to delete the person")
                keyword = readInput(master, "Sökterm: ")
                master.sok("TABORT", keyword)
            elif(userinput1 == "1"):
                #print("#attempt to change person")
                keyword = readInput(master, "Sökterm: ")
                master.sok("ANDRA", keyword)
                
        
        elif(val == '5'):
            master.skrivAndringarTillFil() ##NY FUNKTION, ANVÄND EJ GAMLA
            exit()


            #SPARA ÄNDRINGARNA OCH AVSLUTA SEDAN PROGRAMMET
            #De ändringar som ska sparas är nya kontakter tillagda till de olika registern.
            #Dvs kontakter ska skrivas till respektive register, samt ändringar till befintliga kontakter samt borttagningar.



def huvudMenyInstruktioner():
    print('''
    Vad vill du göra?

(1) Bläddra bland mina register
(2) Skapa ny kontakt
(3) Skapa nytt register
(4) Ändra/ta bort befintlig kontakt
(5) Spara och avsluta programmet.
    ''')


def readInput(master, prompt=""): #master får åka med här för att ifall anv. väljer att avbryta nuvarande operation går programmet tillbaka till startpunkten och master objektet skickas med så att vi inte behöver läsa in alla data igen. (vill undvika globala variabler)
    try:
        userInput = input(prompt)
        if(userInput != "!"):
            return userInput
        else:
            print("\n----------------------\nDu har valt att avbryta nuvarande val, återgår till huvudmenyn.\n")
            huvudMeny(0, master)
    except:
        print("Something went wrong.")
        huvudMeny(0, master)
    


def skapaNyPerson(master):
    #Läser in userinput för värdena, låter anv. välja vilka register som personen ska tillhöra, skapar personen och lägger till den till lämpliga register.
    print("Du har valt att skapa en ny kontakt.")
    fornamn = readInput(master, "Förnamn: ")
    efternamn = readInput(master, "Efternamn: ")
    address = readInput(master, "Address: ")
    telefonnummer = readInput(master, "Telefonnummer: ")
    nyKontakt = Person(fornamn, efternamn, address, telefonnummer)
    
    master.skrivUtRegister()
    val = readInput(master, "Vilket/vilka register vill du lägga till kontakten till?")

    valen = master.valjRegister(val)

    #print("YOUY GOT HERE")
    #print(valen)

    master.laggTillPersonIRegister(nyKontakt, valen)
    






"""

def laggTillPersonIRegister(nyKontakt, listaMedRegisterObj):
    skrivUtRegister(listaMedRegisterObj)    

    val = readInput("Vilket/vilka register vill du lägga till kontakten till?")
    if(len(val) == 1):#kontakten ska bara tilläggas till ett register
        #lägg till nyKontakt till det register som motsvarar valet
        index = int(val)
        listaMedRegisterObj[index-1].laggTillKontakt(nyKontakt)
    else:
        fleraVal = val.split(",")
        for ettVal in fleraVal:
            listaMedRegisterObj[int(ettVal)-1].laggTillKontakt(nyKontakt) #-1 för att userInput är 1 men vi ska lägga till till det 0:te elementet
            #skrivPersonTillRegister(nyKontakt, (namn.get(int(nyttVal[int(val)-1])))[:-1])

def skapaNyttRegister(listaMedRegisterObj):
    namnPaRegister = readInput("Namn på nya registret: ")
    file = open("register.info", "a")
    file.write(namnPaRegister + "\n") #SAK 1
    f= open(namnPaRegister.lower()+".reg","w") #SAK 2
    f.close()
    listaMedRegisterObj.append(Register(namnPaRegister)) #SAK3





def hamtaRegisterNamn():
    file = open("register.info", "r")    
    lines = file.readlines()
    myDict = {}
    for i in range(0, len(lines)):
        line = lines[i]
        line.strip("\n")
        myDict.update({i+1:line})
        #print("("+str(i+1)+") " + lines[i], end="")
    return(myDict)



def skrivUtRegister(listaMedRegisterObj):
    for i in range(0, len(listaMedRegisterObj)):
        print("("+str(i+1)+") "+listaMedRegisterObj[i].getNamn())





def laddaRegisterMedInfoFranFil(listaMedRegisterObj):
    #print(listaMedRegisterObj)
    for i in range(0, len(listaMedRegisterObj)):
        #nyKontakt måste här läsa från relevant register och göra ett nytt kontakt objekt
        filnamn = listaMedRegisterObj[i].getNamn().lower()+".reg"
        fil = open(filnamn, "r")

        data = fil.readlines()
        if(len(data) > 0): #edge case fix
            del data[0]

        for b in range(0, len(data)): #for loopen tar bort ny rad brytning som vi ej vill ha vid nyskapning av personer
            data[b] = data[b].strip("\n") 

        for c in range(0, len(data), 4):
            nyKontakt = Person(data[c], data[c+1], data[c+2], data[c+3])
            listaMedRegisterObj[i].laggTillKontakt(nyKontakt)




def skapaListaMedRegister():
    registerNamn = hamtaRegisterNamn()
    listaMedRegisterObj = [] #DENNA LISTA ÄR VITAL UNDER HELA KÖRNINGEN, GER TILLGÅNG TILL REGISTER, VARPÅ REGISTER GER TILLGÅNG TILL PERSONER
    
    for i in range(0, len(registerNamn.keys())):
        #listaMedRegisterObj.append(Register(registerNamn.get(i)[:-1].lower()+".reg"))
        namn = registerNamn.get(i+1)[:-1]
        listaMedRegisterObj.append(Register(namn))
    return listaMedRegisterObj


def skrivAndringarTillFil(listaMedRegisterObj):
    for register in listaMedRegisterObj:
        filnamn = register.getNamn().lower()+".reg"
        fil = open(filnamn, "w")
        #for i in range(0, len(listaMedRegisterObj)):
        fil.write(register.skrivSamtligDataTillFil())
        fil.close()




"""