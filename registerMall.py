"""
Författare: Fredrik Stoltz
Datum: 
"""


class Register():

    def __init__(self, namn, personLista=None):
        #“””Skapa register”””
        self.__namn = namn
        self.__personLista = [] #denna lista ska innehålla person objekt

    def skrivUtAlla(self):
        #Skriver ut alla personer i sin lista”
        for person in self.__personLista:
            print(person)

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
    
    def sok(self, keyword):
        #Generisk sökfunktion som försöker hitta en matchning av keyword på något i sin personLista, vid flera träffar returneras dessa träffar, vid en träff returneras just den träffen, vid ingen träff returneras (Kunde ej hitta.).
        pass

    def taBortPerson(self, kontakt):
        #“Går igenom sin personLista och tar bort kontakt från den”
        pass