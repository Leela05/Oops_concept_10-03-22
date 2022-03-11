class Person(object):
    def __init__(self,name,aadhar,phoneno):
        self.name = name
        self.aadhar = aadhar
        self.phoneno = phoneno

    def displayDetails(self):
        print(self.name+"\n"+self.aadhar+"\n"+self.phoneno)

class Employee(Person):
    def __init__(self, name, aadhar, phoneno,salary, designation):
        self.salary = salary
        self.designation = designation
        Person.__init__(self,name,aadhar,phoneno)

    def printDetails(self):
        print("Name=",self.name)
        print("Name=",self.aadhar)
        print("Name=",self.phoneno)
        print("Name=",self.salary)
        print("Name=",self.designation)
x = Employee("Amu","1234567890","9566629654","30000","Designer")
x.printDetails()
x.displayDetails()
y = Person("Renu","1235467890","9750188078")

