class Governement:
    def __init__(self):
        self.__price =100

    def viewPetrol(self):
        print(self.__price)

    def hikePrice(self,price):
        self.__price = price

obj = Governement()
obj.viewPetrol()

obj.__price = 130
obj.viewPetrol()

obj.hikePrice(120)
obj.viewPetrol()

print("or")

class Governement:
    def __init__(self,price):
        self.__price = price
    def viewPetrol(self):
        print(self.__price)
    def hikePrice(self,price):
        self.__price = price

obj = Governement(90)
obj.viewPetrol()

obj.__price = 130
obj.viewPetrol()

obj.hikePrice(120)
obj.viewPetrol()

