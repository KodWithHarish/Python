# append file
try:
    with open("file.txt", "a") as file:
        file.write(" Kumbhar")
    # file.close()
except Exception as e:
    print(e)