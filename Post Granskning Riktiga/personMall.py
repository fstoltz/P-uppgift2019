"""
Författare: Fredrik Stoltz
Datum: 17/11-2019
"""
from time import sleep

"""
Person innehåller förnamn, efternamn, address och telefonnummer.
"""
class Person():
    def __init__(self, fornamn, efternamn, address, nummer):
        #“““Skapa personobjekt”””
        self.__fornamn = fornamn
        self.__efternamn = efternamn
        self.__address = address
        self.__nummer = nummer

    #Returnerar förnamnet
    def getFornamn(self):
        return self.__fornamn

    #Returnerar efternamnet
    def getEfternamn(self):
        return self.__efternamn

    #Returnerar addressen
    def getAddress(self):
        return self.__address

    #Returnerar nummret
    def getNummer(self):
        return self.__nummer

    #Sätter adressen till nyAddress inparametern
    def setAddress(self, nyAddress):
        self.__address = nyAddress

    #Sätter nummret till nyttNummer inparametern
    def setNummer(self, nyttNummer):
        self.__nummer = nyttNummer


    #Detta format används för användarvänlig utskrift av personen under programkörning
    def __str__(self):
        sleep(0.7) #lås tråden lite för annars är det svårt ibland att se vad som skrivs ut.
        return  30*"="+"\n"+ self.__fornamn + "\t" + self.__efternamn + ", " + self.__address + ", " + self.__nummer


    #Detta format används då personen ska skrivas till en fil
    def skrivTillFil(self):
        return("\n" +self.__fornamn + "\n" + self.__efternamn + "\n" + self.__address + "\n" + self.__nummer)
        