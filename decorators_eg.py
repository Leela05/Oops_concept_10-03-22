def calculator(fun):
    print("Execute this first")
    def inner(a,b):
        print(a)
        print(b)
        return fun(a,b)
    return inner
@calculator
def add(a,b):
    print(a+b)
add(10,20)