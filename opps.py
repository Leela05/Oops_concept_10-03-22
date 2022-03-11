class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def printData(self):
        print(self.model)
        print(self.color)
        print(self.year)

    def getCustomer(self,name):
        self.name = name

    def printCustomer(self):
         print(self.name)

bmw = Car("3 series", "Red", "2019")
benz = Car("c class", "white", "2020")

bmw.getCustomer("Amu")
bmw.printCustomer()
bmw.printData()
benz.printData()
