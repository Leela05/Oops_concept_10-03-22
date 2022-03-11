class Student():
    def __init__(self, name, rollno, admno, college):
        self.name = name
        self.rollno = rollno
        self.admno = admno
        self.college = college

    def displayDetails(self):
        print(self.name+"\n"+self.rollno+"\n"+self.admno+"\n"+self.college)

class Exam(Student):
    def __init__(self, name, rollno, admno, college, english_mark, math_mark, physics_mark, chemistry_mark):
        self.english_mark = english_mark
        self.math_mark = math_mark
        self.physics_mark = physics_mark
        self.chemistry_mark = chemistry_mark

        Student.__init__(self,name,rollno,admno,college)

    def printDetails(self):
        print("Name:",self.name)
        print("Rollno:", self.rollno)
        print("Admno:", self.admno)
        print("College:",self.college)
        print("english_mark:", self.english_mark)
        print("math_mark:", self.math_mark)
        print("physics_mark:", self.physics_mark)
        print("Chemistry_mark:", self.chemistry_mark)
x = Exam("Leela", "54", "01", "ACE", "99", "100", "89", "99")
x.printDetails()
x.displayDetails()
y = Student("Amu", "207", "04", "KEC")


