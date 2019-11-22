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
        for namn in namnLista:
            self.sok(namn, "LETA")


    def skrivSamtligDataTillFil(self):
        #Returnerar en sträng bestående av en samtliga personers data i detta registers lista.
        data = ""
        for person in self.__personLista:
            data += person.skrivTillFil()
        return data


    def antalPersoner(self):
        return len(self.__personLista)


    def laggTillKontakt(self, nyKontakt):
        self.__personLista.append(nyKontakt)


    def getNamn(self):
        return self.__namn
    

    def sok(self, keyword, typ):
            #Generisk sökfunktion som försöker hitta en matchning av keyword på något i sin personLista, 
            #vid flera träffar(ex. samma förnamn) skrivs samtliga träffar ut, vid en träff skrivs just den träffen ut, vid ingen träff skrivs inget ut.
            keyword = keyword.lower()
            
            for person in self.__personLista:
                if(person.getFornamn().lower() == keyword or person.getEfternamn().lower() == keyword or person.getNummer() == keyword or person.getAddress().lower() == keyword):
                    if(typ == "LETA"):
                        print(person)
                    elif(typ == "TABORT"):
                        print("---> Är du säker på att du vill ta bort " + person.getFornamn() + " " + person.getEfternamn() + "?\n---> Ange 'JA' för att fortsätta.")
                        if(input() == "JA"):
                            self.__personLista.remove(person)
                            print(person.getFornamn() + " " + person.getEfternamn() + " har tagits borts.")
                        else:
                            print("---> Personen har inte tagits bort.")
                    elif(typ == "ANDRA"):
                        #Jag tycker det är viktigare att kunna söka med enkla termer och sen knappa igenom om man hamnade på fel person
                        #än att behöva komma ihåg hela namnet på personen för att kunna ta bort den
                        self.andraPaKontakt(person)
                        print("---------------------\n")


    def andraPaKontakt(self, person):
        #Ändrar på en kontakt. Validerar telefonnummret. Allt som inte är 'ja/JA/jA/Ja' tolkas som ett nej.
        print("---> Du ändrar just nu på kontakten '"+person.getFornamn()+" "+person.getEfternamn()+"'. Är det rätt person?(ja/nej)")
        if(input().lower() == "ja"):
            usrin1 = input("---> Vill du byta telefonnummer(ja/nej)?").lower()
            if(usrin1 == "ja"):
                person.setNummer(funktioner.validateInput(input("Ange nytt nummer: "), "NUM"))
                print("Telefonnummret har uppdaterats.")
            usrin1 = input("---> Vill du byta address(ja/nej)?").lower()
            if(usrin1 == "ja"):
                person.setAddress(funktioner.validateInput(input("Ange ny address: ")), "ADDR")
                print("Addressen har uppdaterats.")
    

    def getPersonLista(self):
        return self.__personLista