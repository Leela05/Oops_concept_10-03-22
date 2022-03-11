class Birds():
     def fly(self):
        print("all birds can fly")
class Pigeon(Birds):
    def fly(self):
        super().fly()
        print("pigeon can fly")

x = Pigeon()
x.fly()



