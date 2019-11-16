"""
Författare: Fredrik Stoltz
Datum: 29/10-2019
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
        #Returnera fornamnet

    def getEfternamn(self):
        return self.__efternamn
        #Returnera efternamnet

    def getAddress(self):
        return self.__address
        #Returnera address

    def getNummer(self):
        return self.__nummer
        #Returnera nummer

    def setAddress(self, nyAddress):
        self.__address = nyAddress
        pass
        #Uppdatera address

    def setNummer(self, nyttNummer):
        #Uppdatera nummer
        self.__nummer = nyttNummer
        pass

    def __str__(self):
        #Detta format används för användarvänlig utskrift av            personen under programkörning
        return  "---------------------\n"+ self.__fornamn + "\n" + self.__efternamn + "\n" + self.__address + "\n" + self.__nummer

    def skrivTillFil(self):
        #Detta format används då personen ska skrivas till en fil
        return("\n" +self.__fornamn + "\n" + self.__efternamn + "\n" + self.__address + "\n" + self.__nummer)
        