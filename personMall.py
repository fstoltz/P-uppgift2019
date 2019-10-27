"""
Författare: Fredrik Stoltz
Datum: 
"""



class Person():

    
    def __init__(self, fornamn, efternamn, address, nummer):
        #“““Skapa personobjekt”””
        self.__fornamn = fornamn
        self.__efternamn = efternamn
        self.__address = address
        self.__nummer = nummer

    def getFornamn(self):
        pass
        #Returnera fornamnet

    def getEfternamn(self):
        pass
        #Returnera efternamnet

    def getAddress(self):
        pass
        #Returnera address

    def getNummer(self):
        pass
        #Returnera nummer

    def setAddress(self, nyAddress):
        pass
        #Uppdatera address

    def setNummer(self, nyttNummer):
        #Uppdatera nummer
        pass

    def __str__(self):
        #Detta format används för användarvänlig utskrift av            personen under programkörning
        pass

    def skrivTillFil(self):
        #Detta format används då personen ska skrivas till en fil
        return(self.__fornamn + "\n" + self.__efternamn + "\n" + self.__address + "\n" + self.__nummer)
        