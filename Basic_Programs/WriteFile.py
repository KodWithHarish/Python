# 2.write file
try:
    with open("file.txt", "w") as file:
        file.write("Harish")
except Exception as e:
    print(e)



