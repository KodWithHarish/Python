import re

name = 'harish'
email = 'harishq8079@gmail.com'
longstring = "my name is harish and i am learning python harishq8079@gmail.com"

# print(re.search(r"[a-zA-Z0-9_]",name)) # \w is equal to [a-zA-Z0-9_]
# print(re.search(r"\w+",name))
# print(re.search(r"\*",name))
# print(re.search(r"\w?",name))
# print(re.search(r"\w*",name).end())
# print(re.search(r"\w*",name).group())
search = re.search(r"[\w\s]*",longstring)
print(search)
