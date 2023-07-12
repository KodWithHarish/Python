import re

# email = 'harishq8079@gmil.com'

# print(re.match(r"[\w@]+gmail.com$",email))

# username = 'Harish-09'

# print(re.match(r"^[a-zA-Z]+[\w-]+[\d]$",username))

# pwd = 'Ha@66777'

# print(re.match(r"^[A-Z]+([a-zA-Z0-9\W]{7,15})+",pwd))

uname= input("Enter Username\n")
pwd = input("Enter Password\n") 

ex=re.compile(r"^[a-zA-Z]+[\w-]+[\d]$")
ex1=ex.findall(uname)

# ex2=re.compile(r"(^[A-Z]+[a-zA-Z0-9]+(@|#|$|%|^|&){2}){7,15}")
ex2=re.compile(r"^[A-Z]+[a-zA-Z0-9\W\W]{7,15}")
ex3=ex2.findall(pwd)
print()
if ex1==[uname]:
    print("valid Username\n")
else:
    print("Invalid Username\n")
if ex3==[pwd]:
    print("valid Password\n")
else:
    print("Invalid Password\n")