"""
Författare: Fredrik Stoltz
Datum: 17/11-2019
"""
from MasterRegisterMall import MasterRegister
from personMall import Person


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
                valen = master.valjRegister(readInput(master, "\n\n---> Vilka register vill du söka inom?\n---> Ex. ange '3' för register nr.3 alt. '3,5,1' för register tre, fem och ett(samkörning).\n---> Ange ENTER för att söka inom samtliga.\n"))
                
                print("\n---> Ange ENTER för att söka utan någon term, dvs alla kontakter skrivs ut(i namnordning).")
                keyword = readInput(master, "Sökterm: ")
            
                master.sok("LETA", keyword, valen)
            except:
                print("Something went wrong...")
            
        

        elif(val == '2'):
            skapaNyPerson(master)
        

        elif(val == '3'):
            master.skapaNyttRegister(readInput(master, "---> Namn på nya registret: "))
        

        elif(val == '4'):
            #Icke-giltig input på raden nedan leder till att anv. slussas tillbaka till huvudmenyn.
            userinput1 = readInput(master, "---> Vill du ändra(1) eller ta bort personen(2)?")
            if(userinput1 == "2"):
                #Ett försök görs till att ta bort en person. (Kan misslyckas om söktermen inte får någon match)
                keyword = readInput(master, "Sökterm: ")
                master.sok("TABORT", keyword)
            elif(userinput1 == "1"):
                #Ett försök görs till att ändra en persons telefonnummer eller address, eller båda två.
                keyword = readInput(master, "Sökterm: ")
                master.sok("ANDRA", keyword)
                
        
        elif(val == '5'):
            #SPARA ÄNDRINGARNA OCH AVSLUTA SEDAN PROGRAMMET
            #De ändringar som ska sparas är nya kontakter tillagda till de olika registern, borttagning av kontakter, uppdateringar av kontakter.
            #Dvs programmets minne som innehåller alla kontakter ska skrivas till respektive registerfil(***.reg).
            master.skrivAndringarTillFil()
            exit()



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
            print("\n----------------------\n---> Du har valt att avbryta nuvarande val, återgår till huvudmenyn.\n")
            huvudMeny(0, master)
    except:
        print("Something went wrong.")
        huvudMeny(0, master)
    


def skapaNyPerson(master):
    #Läser in userinput för värdena, låter anv. välja vilka register som personen ska tillhöra, skapar personen och lägger till den till lämpliga register.
    print("---> Du har valt att skapa en ny kontakt.")
    fornamn = readInput(master, "Förnamn: ")
    efternamn = readInput(master, "Efternamn: ")
    address = readInput(master, "Address: ")
    telefonnummer = readInput(master, master.validateInput(input("Telefonnummer: ")))
    nyKontakt = Person(fornamn, efternamn, address, telefonnummer)
    
    master.skrivUtRegister()
    
    val = readInput(master, "---> Vilket/vilka register vill du lägga till kontakten till?")

    valen = master.valjRegister(val)

    master.laggTillPersonIRegister(nyKontakt, valen)
    