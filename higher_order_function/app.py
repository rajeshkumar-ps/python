def greet():
    print("Hello, World!")
    
def execute_function(func):
    print("before func()")
    func()    
    print("after func()")
execute_function(greet)    