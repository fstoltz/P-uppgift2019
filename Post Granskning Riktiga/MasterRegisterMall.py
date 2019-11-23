"""
Författare: Fredrik Stoltz
Datum: 17/11-2019
"""
from registerMall import Register
from personMall import Person
import funktioner
import os

# NOTERA: 
# anv. = användaren
# ANDRA = ÄNDRA

"""
Klass som endast får instansieras en gång! (Singleton design pattern(tanken åtminstone))
Denna klass innehåller en lista, där objekten består av de olika registrena.
Detta är "Master"-klassen och tanken är att denna kontrollerar mycket av de "större" valen,
och dessa val förverkligas sedan av m.h.a klasserna Register och Person.
"""
class MasterRegister:
    def __init__(self):
        self.__huvudRegister = []


    #Generisk sökfunktion som tar emot ett keyword och ett antal val som argument,
    # baserat på dessa anv. metoden if-satser för att avgöra vilken utskrift som ska användas.
    def sok(self, typ, keyword, valen=None):
        
        matchStatusPerRegister = [] #Denna lista används för att avgöra ifall ingen träff har skett i något av alla register.
        if(valen == None): 
            valen = self.valjAllaRegister() #Vid ändring och borttagning söks inom samtliga register.
            

        if(typ == "LETA" and len(self.__huvudRegister) != 0): # len != 0 hanterar det fall då det inte finns några register, då ska det inte ske någon sökning.
            for val in valen:
                print("\n\n|||*****"+self.__huvudRegister[val].getNamn()+"*****|||")
                if(len(keyword) == 0): #Ingen sökterm angavs, skriver därmed ut samtliga.
                    self.__huvudRegister[val].skrivUtAlla()
                else:                  #Sökterm angavs och finns i keyword, som används av det aktuella registrets sökfunktion.
                    matchStatusPerRegister.append(self.__huvudRegister[val].sok(keyword, "LETA")) #Appendar "False/True" för varje sökning. Om listan tillslut bara består av False vet jag att ingen träff har skett och kan skriva ut ETT meddelande at ingen träff skett.
                print("|||********************|||")

        elif(typ == "ANDRA" and len(self.__huvudRegister) != 0):
            #Ändra på persons info mha keyword
            for val in valen:
                matchStatusPerRegister.append(self.__huvudRegister[val].sok(keyword, "ANDRA"))

        elif(typ == "TABORT" and len(self.__huvudRegister) != 0):
            #Ta bort personen mha keyword            
            for val in valen:
                matchStatusPerRegister.append(self.__huvudRegister[val].sok(keyword, "TABORT"))
        #Kolla ifall det har skett en träff eller inte.
        if(typ != "LETA"): #tar hand om både TABORT och ANDRA=ÄNDRA
            self.traffEllerInte(matchStatusPerRegister, typ)
        if(typ == "LETA" and len(keyword) != 0):
            self.traffEllerInte(matchStatusPerRegister, "LETA", valen)

        #Om ingen träff skedde ger vi en chans till anv. att försöka igen, utan att knappa sig igenom huvudmenyn på nytt för att göra samma sökning med ny sökterm.
        self.sokaIgen(typ, valen)

    #Om alla sökningar resulterade i att registerfunktionens sökfunktion returnerade "False" har ingen träff skett.
    def traffEllerInte(self, lista, typ, valen=None):
        if(all(match == False for match in lista)): #REFERENS för kod https://stackoverflow.com/questions/3525953/check-if-all-values-of-iterable-are-zero
            print("\n---> [INGEN TRÄFF]\n")


    #Funktion som returnerar en "val-lista" med där samtliga register är med.
    def valjAllaRegister(self):
        valen = []
        for i in range(0, len(self.__huvudRegister)):
            valen.append(i) #vid borttagning eller ändring används samtliga register för att söka
        return valen


    #Låter användaren söka igenom med samma val som innan, dvs för att göra ytterliggare en sökning
    #inom ex. samma register utan att behöva gå via huvudmenyn på nytt.
    def sokaIgen(self, typ, valen=None):
        print("\n\n---> Vill du söka igen(ja/nej)?")
        if(self.readInput().lower() == "ja"):
            self.sok(typ, self.readInput("Sökterm: "), valen)


    #Körs en gång per programkörning. 
    #Körs i början för att skapa register med deras korrekta namn(namnet används sedan för att hitta rätt fil då registret laddas med data).
    def skapaRegisterMedRespNamn(self):
        registerNamn = self.hamtaRegisterNamn()
        for i in range(0, len(registerNamn.keys())):
            namn = registerNamn.get(i+1)#[:-1] # [:-1] Ignorerar '\n' som kommer från 'register.info' inläsningen.
            self.__huvudRegister.append(Register(namn))


    #Hämtar registernamn från filen 'register.info'. Ifall detta misslyckas stängs programmet ned eftersom detta är en vital del av programmet.
    def hamtaRegisterNamn(self):
        try:
            file = open("register.info", "r")    
            lines = file.readlines()
            numAndNameDict = {}
            for i in range(0, len(lines)):
                line = lines[i]
                numAndNameDict.update({i+1:line.strip("\n")})
            #Såhär ser dictionaryn typisk ut här: {1: 'KTH', 2: 'Familj', 3: 'Simning'}
            return(numAndNameDict)
        except FileNotFoundError:
            print("\n\n\n---> Filen som innehåller namnen på de olika registrena kunde inte hittas. Vänligen återställ filen 'register.info'")
            print("---> Avslutar...")
            exit()
        

    #Denna funktion körs då anv. valt att avsluta programmet. Då skrivs samtliga ändringar gjorda under körningen till respektive '-----.reg' fil.
    def skrivAndringarTillFil(self):
        for register in self.__huvudRegister:
            filnamn = self.taBortSvenskaBokstaver(register.getNamn()).lower()+".reg"
            fil = open(filnamn, "w")
            fil.write(register.skrivSamtligDataTillFil())
            fil.close()

    #Ersätter å,ä,ö med a, ae, o.
    def taBortSvenskaBokstaver(self, text):
        rensadText = ""
        for char in text:
            if(char == 'å'):
                char = 'a'
            elif(char == 'ö'):
                char = 'o'
            elif(char == 'ä'):
                char = 'ae'
            rensadText += char
        return rensadText

    #Skapar ett nytt register, lägger till(append) till namnet i 'register.info' samt skapar filen '----.reg'
    #Skapar sedan ett nytt Register och lägger till det till masterns huvudregister.
    def skapaNyttRegister(self, namnPaRegister):
        if (self.kontrolleraFilensExistens("register.info") == True):
            file = open("register.info", "a") #delmoment 1
             
            file.write(namnPaRegister + "\n") 
            file.close()
            
            f = open(self.taBortSvenskaBokstaver(namnPaRegister).lower()+".reg","w") #delmoment 2
            f.close()
            self.__huvudRegister.append(Register(namnPaRegister)) #delmoment 3
            print("\n---> Ett nytt register '"+namnPaRegister+"' har skapats.")
        else:
            print("---> Filen 'register.info' har korrumpterats under programmets körning. Vänligen återställ den.")


    #Kontrollerar namnet på filerna i programmets katalog för att garantera att filen finns innan en fil-läsning initieras.
    def kontrolleraFilensExistens(self, filnamn):
        contents = os.listdir(os.getcwd()) #REFERENS FÖR KOD: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
        if filnamn in contents:
            return True
        else:
            return False


    #Lägger till nyKontakt till de register som användaren valt.
    #valen är vilka register anv. valde att lägga till nyKontakt till
    def laggTillPersonIRegister(self, nyKontakt, valen):
        for val in valen:
            self.__huvudRegister[val].laggTillKontakt(nyKontakt)


    #Anv. har presenterats med samtliga register och får nu välja vilka som ska användas(ex. vid sökning, skapa ny kontakt).
    def valjRegister(self, val):
        
        lista = []
        if(val == ""): #hanterar ett 'ENTER' input, tolkas som att anv. valt SAMTLIGA register
            for i in range(0, len(self.__huvudRegister)):
                lista.append(i)
        else:
            valen = val.split(",") #Kommaseparerad input för att välja flera register
            for val in valen:
                index = int(val)
                
                while(index not in range(1, len(self.__huvudRegister)+1)):
                    print(str(index)+" är inte associerat med något register. Försök igen.")
                    index = int(input("Svar: "))
                lista.append(index-1) #minus ett ty listan kommer användas för att indexera andra listor och då slipper jag göra det på flera ställen(räcker att göra det här).
        return lista


    #Skriver ut samtliga register, med ett sifferindex till vänster för att underlätta valen från anv.
    def skrivUtRegister(self):
        for i in range(0, len(self.__huvudRegister)):
            print("\n("+str(i+1)+") "+self.__huvudRegister[i].getNamn())
            #+"\nAntal personer: "+str(self.__huvudRegister[i].antalPersoner()


    #Metod som laddar alla register med respektive data från deras '---.reg' fil.
    #i, b, c är iteratorer
    def laddaAllaRegisterMedInfoFranFil(self):
        for i in range(0, len(self.__huvudRegister)):
            filnamn = self.taBortSvenskaBokstaver(self.__huvudRegister[i].getNamn()).lower()+".reg"
            if (self.kontrolleraFilensExistens(filnamn) == True):
                fil = open(filnamn, "r")
                data = fil.readlines()

                if(len(data) > 0): #edge case fix(radbrytning i början av filen)
                    del data[0]

                for b in range(0, len(data)): #for loopen tar bort ny rad brytning som vi ej vill ha vid nyskapning av personer
                    data[b] = data[b].strip("\n") 

                for c in range(0, len(data), 4): #fyra rader per person
                    nyKontakt = Person(data[c], data[c+1], data[c+2], data[c+3])
                    self.__huvudRegister[i].laggTillKontakt(nyKontakt)
            else: #Om en enskild registerfil inte fanns varnas anv. om detta. (Ej vital del av programmet, så körningen fortsätter)
                print("\n\n---> Filen '"+filnamn+"' kunde inte hittas. Vänligen återställ den.")


    #Läser in userinput för värdena, låter anv. välja vilka register som personen ska tillhöra,
    #skapar personen och lägger till den till respektive register som anv. valt.
    def skapaNyPerson(self):
        print("---> Du har valt att skapa en ny kontakt.")
        fornamn = self.readInput("Förnamn: ")
        efternamn = self.readInput("Efternamn: ")
        address = self.readInput("Address: ")
        telefonnummer = funktioner.validateInput(self.readInput("Telefonnummer: "), "NUM")
        nyKontakt = Person(fornamn, efternamn, address, telefonnummer)
        #nyKontakt = Person(fornamn, efternamn, address, funktioner.validateInput(telefonnummer, "NUM"))
        
        self.skrivUtRegister()
        val = self.readInput("---> Vilket/vilka register vill du lägga till kontakten till?\n---> Ex. 4,2 för att lägga till kontakten till register fyra och två.\nSvar: ")
        valen = self.valjRegister(val)
        self.laggTillPersonIRegister(nyKontakt, valen)
        print("Kontakten '"+fornamn+" "+efternamn+"' har skapats.")


    #Inläsningsfunktion som garanterar att användaren närsomhelst kan återgå till huvudmenyn genom att ange '!' som input.
    def readInput(self, prompt=""): 
        try:
            userInput = input(prompt)
            if(userInput != "!"):
                return userInput
            else:
                print("\n----------------------\n---> Du har valt att avbryta nuvarande val, återgår till huvudmenyn.\n")
                funktioner.huvudMeny(0, self)#self får åka med här för att ifall anv. väljer att avbryta nuvarande operation går programmet tillbaka till startpunkten och
                #self objektet skickas således med så att vi inte behöver läsa in all data igen. (vill undvika globala variabler i funktioner filen)
        except:
            print("Något gick fel vid inläsning.")
            funktioner.huvudMeny(0, self)