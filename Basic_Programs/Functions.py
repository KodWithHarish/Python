# function
def sum(a,b):
    return a+b

print(sum(10,20))

# nested function
def outerfunction():
    print("\ni am outer function")
    def innerfunction():
        print("i am inner/nested function")
    innerfunction()

outerfunction()
