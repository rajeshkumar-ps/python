import time


def measure_time(func,args,kwargs):
    start = time.time()
    func(*args, **kwargs) #args method is used to pass non-keyworded variable length argument list to the function and kwargs method is used to pass keyworded variable length argument list to the function
    end = time.time()
    print(f"Execution Time: {end - start} seconds")

def power(limit,name):
    print(f"Function executed by {name}")
    return [x**2 for x in range(limit)]

measure_time(power,(1000000,),{'name':'rajesh'})
