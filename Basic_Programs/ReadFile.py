# files
# 1.read file
file = open("file.txt", "r")
print(file.read())
# print(file.readline())
# print(file.readline())
print(file.readline(3))
# print(len(file.readlines()))


# except
try:
    file = open("python.txt")
    print(file.read())
except:
    print('something went wrong')

# Exception
try:
    file = open("python.txt")
    print(file.read())
except Exception as e:
    print(e)
