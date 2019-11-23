"""
Författare: Fredrik Stoltz
Datum: 17/11-2019
"""
import funktioner

"""
Register består av en lista som innehåller Person objekt.
"""
class Register():
    def __init__(self, namn, personLista=None):
        self.__namn = namn
        self.__personLista = [] #denna lista ska innehålla person objekt


    def skrivUtAlla(self):
        #Skriver ut alla personer i sin lista i bokstavsordning(baserat på förnamn)
        namnLista = []
        for person in self.__personLista:
            namnLista.append(person.getFornamn())
        namnLista.sort()
        antalKontakterIRegistret = len(namnLista)
        if(antalKontakterIRegistret == 0):
            print("Registret är tomt...")
        else:
            print("Antal kontakter i registret: "+str(antalKontakterIRegistret))
        senasteNamnet = None #senasteNamnet hanterar ett edge case fix då flera personer har samma förnamn(utan detta så skulle det ske duplikata utskrifter av samma person)
        #Om det ex. finns två personer med samma förnamn så kommer en iteration genom for-loopen skriva ut båda två.
        for namn in namnLista:
            if(senasteNamnet != namn):
                self.sok(namn, "LETA")
            senasteNamnet = namn
        

    #Returnerar en sträng bestående av en samtliga personers data i detta registers lista.
    def skrivSamtligDataTillFil(self):
        data = ""
        for person in self.__personLista:
            data += person.skrivTillFil()
        return data

    #Returnerar antal kontakter i sin personobjektslista
    def antalPersoner(self):
        return len(self.__personLista)

    #Lägger till en kontakt till sin personobjektslista
    def laggTillKontakt(self, nyKontakt):
        self.__personLista.append(nyKontakt)

    #Returnerar registrets namn
    def getNamn(self):
        return self.__namn
    

    #Generisk sökfunktion som försöker hitta en matchning av keyword på något i sin personLista, 
    #vid flera träffar(ex. samma förnamn) skrivs samtliga träffar ut, vid en träff skrivs just den träffen ut, vid ingen träff skrivs inget ut.
    def sok(self, keyword, typ):
            keyword = keyword.lower()
            match = False
            for person in self.__personLista:
                if(person.getFornamn().lower() == keyword or
                 person.getEfternamn().lower() == keyword or
                 person.getNummer() == keyword or
                 person.getAddress().lower() == keyword or
                 (person.getFornamn().lower() + " " + person.getEfternamn().lower()) == keyword):

                    match = True
                
                    if(typ == "LETA"):
                        print(person)
                    elif(typ == "TABORT"):
                        print("---> Är du säker på att du vill ta bort '" + person.getFornamn() + " " + person.getEfternamn() + "' från registret '" + self.getNamn() + "'?\n---> Ange 'ja' för att fortsätta. Ange '!' för att avbryta.")
                        if(input().lower() == "ja"):
                            self.__personLista.remove(person)
                            print(person.getFornamn() + " " + person.getEfternamn() + " har tagits borts.")
                        else:
                            print("---> Personen har inte tagits bort.")
                    elif(typ == "ANDRA"):
                        #Jag tycker det är viktigare att kunna söka med enkla termer och sen knappa igenom om man hamnade på fel person
                        #än att behöva komma ihåg hela namnet på personen för att kunna ta bort den
                        self.andraPaKontakt(person)
                        print("---------------------\n")
            if(match == False and typ == "LETA"):
                print("Ingen träff i registret: "+self.getNamn())
            return match


    #Ändrar på en kontakt. Validerar telefonnummret. Allt som inte är 'ja/JA/jA/Ja' tolkas som ett nej.
    def andraPaKontakt(self, person):
        print("---> Du ändrar just nu på kontakten '"+person.getFornamn()+" "+person.getEfternamn()+"' från registret '"+self.getNamn()+"'. Är det rätt person?(ja/nej)")
        if(input().lower() == "ja"):
            usrin1 = input("---> Vill du byta telefonnummer(ja/nej)?").lower()
            if(usrin1 == "ja"):
                person.setNummer(funktioner.validateInput(input("Ange nytt nummer: "), "NUM"))
                print("Telefonnummret har uppdaterats.")
            usrin1 = input("---> Vill du byta address(ja/nej)?").lower()
            if(usrin1 == "ja"):
                person.setAddress(funktioner.validateInput(input("Ange ny address: ")), "ADDR")
                print("Addressen har uppdaterats.")
    
    #Returnerar registrets personobjektslista
    def getPersonLista(self):
        return self.__personLista