"""
Författare: Fredrik Stoltz
Datum: 17/11-2019
"""

from MasterRegisterMall import MasterRegister


"""
Denna fil består av funktioner som ordnar med menyhantering och validering av input från användaren.
"""



def huvudMeny(firstTime=1, master=None):
    #Skriver ut menyn etc, läser userinput för val. Ropar på lämplig funktion x vid val x, samt skriver ut nödvändig info vid respektive val.
    if(firstTime == 1):
        print("\n\nVälkommen till din kontaktbok.")
        master = MasterRegister()
        master.skapaRegisterMedRespNamn()
        master.laddaAllaRegisterMedInfoFranFil()
    while(1):
        print("_"*86+"\n   Glöm inte att du närsomhelst kan ange '!' för komma tillbaka till huvudmenyn.   \n"+"_"*86)
        huvudMenyInstruktioner()
        val = master.readInput("Svar: ")
        if(val == '1'):
            try:
                master.skrivUtRegister()
                valen = master.valjRegister(master.readInput("\n\n---> Vilka register vill du söka inom?\n---> Ex. ange '3' för register nr.3 alt. '3,5,1' för register tre, fem och ett(samkörning).\n---> Ange ENTER för att söka inom samtliga.\nSvar: "))
                print("\n---> Ange ENTER för att söka utan någon term, dvs alla kontakter skrivs ut(i namnordning).")
                keyword = master.readInput("---> Du kan söka på förnamn, efternamn, address eller telefonnummer.\nSökterm: ")
                master.sok("LETA", keyword, valen)
            except:
                print("Något gick fel...")
            
        elif(val == '2'):
            try:
                master.skapaNyPerson()    
            except:
                print("Något gick fel...")
            
        elif(val == '3'):
            namnPaRegister = master.readInput("---> Namn på nya registret: ")
            while(master.kontrolleraFilensExistens(master.taBortSvenskaBokstaver(namnPaRegister.lower())+".reg") == True):#Register med detta namn finns redan! Kan ej skapa ett nytt!
                print("---> Det finns redan ett register med det önskade namnet, vänligen välj ett annat namn.\n")
                namnPaRegister = master.readInput("Nytt namn: ")
            master.skapaNyttRegister(namnPaRegister)

        elif(val == '4'):
            #Icke-giltig input på raden nedan leder till att anv. slussas tillbaka till huvudmenyn.
            userinput1 = master.readInput("\n(1) Ändra på kontakt\n(2) Ta bort person\nSvar: ")
            if(userinput1 == "2"):
                #Ett försök görs till att ta bort en person. (Kan misslyckas om söktermen inte får någon match)
                keyword = master.readInput("---> Du kan söka på förnamn, efternamn, address eller telefonnummer.\nSökterm: ")
                master.sok("TABORT", keyword)
            elif(userinput1 == "1"):
                #Ett försök görs till att ändra en persons telefonnummer eller address, eller båda två.
                keyword = master.readInput("---> Du kan söka på förnamn, efternamn, address eller telefonnummer.\nSökterm: ")
                master.sok("ANDRA", keyword)
        
        elif(val == '5'):
            #SPARA ÄNDRINGARNA OCH AVSLUTA SEDAN PROGRAMMET
            #De ändringar som ska sparas är nya kontakter tillagda till de olika registern, borttagning av kontakter, uppdateringar av kontakter.
            #Dvs programmets minne som innehåller alla kontakter ska skrivas till respektive registerfil(***.reg).
            master.skrivAndringarTillFil()
            print("Skriver till fil...\nAvslutar programmet...")
            exit() #Stänger av programmet.


def huvudMenyInstruktioner():
    print('''
    Vad vill du göra?

(1) Bläddra bland mina register
(2) Skapa ny kontakt
(3) Skapa nytt register
(4) Ändra/ta bort befintlig kontakt
(5) Spara och avsluta programmet.
    ''')


def validateInput(theInput, typ):
    #Validerar input från användaren. Om "bokstaven" är en siffra, tolkas den som en del av nummret, annars dumpas den.
    if(typ == "NUM"):
        theInput.strip()
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cleanedInput = ""
        for char in theInput:
            if char in numbers:
                cleanedInput += char
    elif(typ == "NAME"):
        pass #(valt att inte sätta några restriktioner på namnsättning, likt en papperskontaktbok)
    return cleanedInput

