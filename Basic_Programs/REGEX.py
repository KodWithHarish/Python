# REGEX
import re

name = 'harish'
email = 'harishq8079@gmail.com'
longstring = "my name is harish and i am learning python harishq8079@gmail.com"

print(re.search(r"[a-zA-Z0-9_]",name)) # \w is equal to [a-zA-Z0-9_]
print(re.search(r"\w+",name))
print(re.search(r"\*",name))
print(re.search(r"\w?",name))
print(re.search(r"\w*",name).end())
print(re.search(r"\w*",name).group())

# long string
search = re.search(r"[\w\s]*",longstring)
print(search)
search1 = re.search(r"my[\w\s]*",longstring)
print(search1.group())

search2 = re.search(r"(my|your)[\w\s]*",longstring)
print(search2.group())

# email string
search2 = re.search(r"\w+@\w+\.com",longstring)
print(search2.group())

# match function
search2 = re.match(r"\w+@\w+\.com",email)
print(search2.group())

# task
import re
emails = "xyz$name123@email.com,xyz#name123@email.net,xyz!name123@email.pk"
email1 = 'xyz$name123@email.com'
email2 = 'xyz#name123@email.net'
email3 = 'xyz!name123@email.pk'

search2 = re.match(r"[\w$#!]+@\w+\.(com|net|pk)",email2)
print(search2.group())

# findall function
search = re.findall(r"[\w$#!]+@\w+\.(com|net|pk)",emails)
print(search)

search = re.findall(r"([\w$#!]+@\w+\.)(com|net|pk)",emails)
print(search)

# find iterative
search = re.finditer(r"[\w$#!]+@\w+\.(com|net|pk)",emails)
for object in search:
    print(object)

# split function
longstring = "my name is harish and i am learning python"
search = re.split(r"\s",longstring)
print(search)

longstring = "my name is harish and i am learning python"
search = re.split(r"am",longstring)
print(search)
