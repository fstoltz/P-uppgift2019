"""
Författare: Fredrik Stoltz
Datum: 29/10-2019
"""
import time

class Register():

    def __init__(self, namn, personLista=None):
        #“””Skapa register”””
        self.__namn = namn
        self.__personLista = [] #denna lista ska innehålla person objekt


    def skrivUtAlla(self):
        #Skriver ut alla personer i sin lista”
        namnLista = []
        for person in self.__personLista:
            #print("---------------------")
            #print(person)
            namnLista.append(person.getFornamn())

        namnLista.sort()
        #print(namnLista)

        #print(self.__personLista)
        
        for namn in namnLista:
            self.sok(namn, "LETA")


        print("---------------------")

    def skrivSamtligDataTillFil(self):
        data = ""
        for person in self.__personLista:
            data = data + person.skrivTillFil()
        return data

    def antalPersoner(self):
        return len(self.__personLista)


    def laggTillKontakt(self, nyKontakt):
        self.__personLista.append(nyKontakt)

    def getNamn(self):
        return self.__namn
    
    def sok(self, keyword, typ):
        #print(keyword + "AR HAR")
        #Generisk sökfunktion som försöker hitta en matchning av keyword på något i sin personLista, vid flera träffar returneras dessa träffar, vid en träff returneras just den träffen, vid ingen träff returneras (Kunde ej hitta.).
        keyword = keyword.lower()
        
        for person in self.__personLista:
            if(person.getFornamn().lower() == keyword or person.getEfternamn().lower() == keyword or person.getNummer() == keyword or person.getAddress().lower() == keyword):
                if(typ == "LETA"):
                    print(person)
                elif(typ == "TABORT"):
                    self.__personLista.remove(person)
                    print(person.getFornamn() + " " + person.getEfternamn() + " har tagits borts.")
                elif(typ == "ANDRA"):
                    #Jag tycker det är viktigare att kunna söka med enkla termer och sen knappa igenom om man hamnade på fel person
                    #än att behöva komma ihåg hela namnet på personen för att kunna ta bort den
                    self.andraPaKontakt(person)

                    print("---------------------\n")


    def andraPaKontakt(self, person):
        print("Du ändrar just nu på kontakten '"+person.getFornamn()+" "+person.getEfternamn()+"'. Är det rätt person?(ja/nej)")
        if(input().lower() == "ja"):
            usrin1 = input("Vill du byta telefonnummer(ja/nej)?").lower()
            if(usrin1 == "ja"):
                person.setNummer(self.validateInput(input("Ange nytt nummer: "), "NUM"))
                print("Telefonnummret har uppdaterats.")
            usrin1 = input("Vill du byta address(ja/nej)?").lower()
            if(usrin1 == "ja"):
                person.setAddress(input("Ange ny address: "))
                print("Addressen har uppdaterats.")



    def validateInput(self, theInput, typ):
        if(typ == "NUM"):
            theInput.strip()
            numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            cleanedInput = ""
            for char in theInput:
                if char in numbers:
                    cleanedInput += char
        return cleanedInput

    def getPersonLista(self):
        return self.__personLista

    def taBortPerson(self, kontakt):
        #“Går igenom sin personLista och tar bort kontakt från den”
        pass