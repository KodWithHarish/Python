# decorator
def decorator(function):
    def wrapper():  # *args
        print("Good Morning,")
        function()  # *args
        print("Have a nice day\n")
    return wrapper
@decorator
def myname():  # name
    print("Harish")    # name
# replace @decorator by myname = decorator(myname)
myname()  # Tejal

# position arguments & keyword arguments
def decorator(function):
    def wrapper(*args,**kwargs):
        print("Good Morning,")
        function(*args,**kwargs)
        print("Have a nice day")
    return wrapper
@decorator
def myname(name,key):
    print(name)
    print(key)
# replace @decorator by myname = decorator(myname)
myname("tejal",key="harish")
