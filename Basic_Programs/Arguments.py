# types of arguments
# 1.Positional arguments : int,float,string,dictionary,tuple
# 2.Keyword

# positional arguments
def function(argument1,argument2,argument3):
    print(argument1,argument2)
    argument3()

def name():
    print("harish")

function((1,2), [1,2,"str"], name)

# keyword arguments
def function(key1):
    print(key1)

function(key1 = 'string')

# more than one keys
def function(key1,key2,key3):
    print(key1,key2,key3)

function(10,key2='string',key3=[1,2,3])

# multi arguments
def multi(*args):
    print(args)

multi(10,20,30,40)

# add all values in multi arguments
def add(*args):
    sum = 0;
    for value in args:
        sum += value
    return sum

print(add(10,20,40))

# keyword arguments
def add(*args ,**kwargs):
   print(args)
   print(kwargs)

add(10,20,40,a=2,b='string')

