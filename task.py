class Student:
    def __init__(self, name, rollno, admino, college):
        self.name = name
        self.rollno = rollno
        self.admino = admino
        self.college = college

    def printData(self):
        print(self.name)
        print(self.rollno)
        print(self.admino)
        print(self.college)

student1= Student(input("enter the student name:"),input("enter the student rollno:"),input("enter the student admino:"),input("enter the student college:"))


student1.printData()