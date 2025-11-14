
def square(x):
    return x * x
def execcute(func):
    func()
execcute(lambda: print(square(5)))    