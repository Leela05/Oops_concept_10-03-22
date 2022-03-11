def hello(fun):
    fun()

def printname():
    print("amu")
display = hello(printname)

#example 1

def hello(fun):
    print("execute this first")
    fun()
@hello
def printname():
    print("amu")




