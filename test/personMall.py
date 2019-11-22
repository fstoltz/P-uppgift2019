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

    def getFornamn(self):
        return self.__fornamn


    def getEfternamn(self):
        return self.__efternamn


    def getAddress(self):
        return self.__address


    def getNummer(self):
        return self.__nummer


    def setAddress(self, nyAddress):
        self.__address = nyAddress


    def setNummer(self, nyttNummer):
        self.__nummer = nyttNummer


    def __str__(self):
        #Detta format används för användarvänlig utskrift av personen under programkörning
        sleep(0.7) #lås tråden lite för annars är det svårt ibland att se vad som skrivs ut.
        return  "------------\n"+ self.__fornamn + "\n" + self.__efternamn + "\n" + self.__address + "\n" + self.__nummer


    def skrivTillFil(self):
        #Detta format används då personen ska skrivas till en fil
        return("\n" +self.__fornamn + "\n" + self.__efternamn + "\n" + self.__address + "\n" + self.__nummer)
        