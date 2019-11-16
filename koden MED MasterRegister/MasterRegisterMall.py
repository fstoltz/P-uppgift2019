"""
Författare: Fredrik Stoltz
Datum: 16/11-2019
"""
from registerMall import Register
from personMall import Person
import funktioner


#Klass som endast får instansieras en gång! (Singleton)
class MasterRegister:

    def __init__(self):
        self.__huvudRegister = []




    def sok(self, typ, keyword, valen=None):
        #print(valen)

        if(valen == None): #vid borttagning eller ändring används samtliga register
            valen = []
            for i in range(0, len(self.__huvudRegister)):
                valen.append(i)
            #print(valen)

        if(typ == "LETA" and len(self.__huvudRegister) != 0):        
            if(len(keyword) == 0): #Ingen sökterm angavs, sök inom alla
                for val in valen:
                    print("\n\n*****  "+self.__huvudRegister[val].getNamn()+"  *****")
                    self.__huvudRegister[val].skrivUtAlla()
            else:
                for val in valen:
                    print("*****  "+self.__huvudRegister[val].getNamn()+"  *****")
                    self.__huvudRegister[val].sok(keyword, "LETA")
        elif(typ == "ANDRA" and len(self.__huvudRegister) != 0):
            #ändra på persons grejjer mha keyword
            for val in valen:
                self.__huvudRegister[val].sok(keyword, "ANDRA")
        elif(typ == "TABORT" and len(self.__huvudRegister) != 0):
            #ta bort personen mha keyword
            #print("Jag kom hit!**********")
            for val in valen:
                self.__huvudRegister[val].sok(keyword, "TABORT")



    def skapaRegisterMedRespNamn(self):
        registerNamn = self.hamtaRegisterNamn()
        listaMedRegisterObj = [] #DENNA LISTA ÄR VITAL UNDER HELA KÖRNINGEN, GER TILLGÅNG TILL REGISTER, VARPÅ REGISTER GER TILLGÅNG TILL PERSONER
    
        for i in range(0, len(registerNamn.keys())):
            #listaMedRegisterObj.append(Register(registerNamn.get(i)[:-1].lower()+".reg"))
            namn = registerNamn.get(i+1)[:-1]
            self.__huvudRegister.append(Register(namn))
        #return listaMedRegisterObj


    def hamtaRegisterNamn(self):
        file = open("register.info", "r")    
        lines = file.readlines()
        myDict = {}
        for i in range(0, len(lines)):
            line = lines[i]
            line.strip("\n")
            myDict.update({i+1:line})
            #print("("+str(i+1)+") " + lines[i], end="")
        return(myDict)


    def skrivAndringarTillFil(self):
        for register in self.__huvudRegister:
            filnamn = register.getNamn().lower()+".reg"
            fil = open(filnamn, "w")
            #for i in range(0, len(listaMedRegisterObj)):
            fil.write(register.skrivSamtligDataTillFil())
            fil.close()


    def skapaNyttRegister(self, namnPaRegister):
        #namnPaRegister = funktioner.readInput(self, "Namn på nya registret: ")
        file = open("register.info", "a")
        file.write(namnPaRegister + "\n") #SAK 1
        f= open(namnPaRegister.lower()+".reg","w") #SAK 2
        f.close()
        self.__huvudRegister.append(Register(namnPaRegister)) #SAK3




    def laggTillPersonIRegister(self, nyKontakt, valen):
        #valen är vilka register anv. valde att lägga till nyKontakt till
        for val in valen:
            self.__huvudRegister[val].laggTillKontakt(nyKontakt)



    def valjRegister(self, val):
        lista = []
        if(val == ""): #hanterar ett ENTER input, tolkas som att anv. valt SAMTLIGA register
            for i in range(0, len(self.__huvudRegister)):
                lista.append(i)
        else:
            valen = val.split(",")
            for val in valen:
                lista.append(int(val)-1) #minus one because this will be used to index lists(this way I don't have to do it at the other places)
        return lista



    def skrivUtRegister(self):
        for i in range(0, len(self.__huvudRegister)):
            print("\n("+str(i+1)+") "+self.__huvudRegister[i].getNamn()+"\nAntal personer: "+str(self.__huvudRegister[i].antalPersoner()))

    def laddaAllaRegisterMedInfoFranFil(self):
    #print(listaMedRegisterObj)
        for i in range(0, len(self.__huvudRegister)):
            #nyKontakt måste här läsa från relevant register och göra ett nytt kontakt objekt
            filnamn = self.__huvudRegister[i].getNamn().lower()+".reg"
            fil = open(filnamn, "r")

            data = fil.readlines()
            if(len(data) > 0): #edge case fix
                del data[0]

            for b in range(0, len(data)): #for loopen tar bort ny rad brytning som vi ej vill ha vid nyskapning av personer
                data[b] = data[b].strip("\n") 

            for c in range(0, len(data), 4):
                nyKontakt = Person(data[c], data[c+1], data[c+2], data[c+3])
                self.__huvudRegister[i].laggTillKontakt(nyKontakt)













"""
    def skapaNyPerson(self):
        #Läser in userinput för värdena, låter anv. välja vilka register som personen ska tillhöra, skapar personen och lägger till den till lämpliga register.
        print("Du har valt att skapa en ny kontakt.")
        fornamn = readInput("Förnamn: ")
        efternamn = readInput("Efternamn: ")
        address = readInput("Address: ")
        telefonnummer = readInput("Telefonnummer: ")
        nyKontakt = Person(fornamn, efternamn, address, telefonnummer)
        self.laggTillPersonIRegister(nyKontakt)
        #self.laggTillPersonIRegister(nyKontakt, listaMedRegisterObj)


#########
        if(len(val) == 1):#kontakten ska bara tilläggas till ett register
            #lägg till nyKontakt till det register som motsvarar valet
            index = int(val)
            lista = []
            lista.append(index)
            return lista
            #self.__huvudRegister[index-1].laggTillKontakt(nyKontakt)
        else:
            fleraVal = val.split(",")
            for element in fleraVal:
                element = int(element)
            return fleraVal
            #for ettVal in fleraVal:
                #self.__huvudRegister[int(ettVal)-1].laggTillKontakt(nyKontakt) #-1 för att userInput är 1 men vi ska lägga till till det 0:te elementet
                #skrivPersonTillRegister(nyKontakt, (namn.get(int(nyttVal[int(val)-1])))[:-1])









    def readInput(self, prompt=""):
        userInput = input(prompt)
        if(userInput != "!"):
            return userInput
        else:
            print("\nDu har valt att avbryta nuvarande val, återgår till huvudmenyn.\n")
            print("FIXXA HÄÄÄR!!!")
            #huvudMeny(0)



"""