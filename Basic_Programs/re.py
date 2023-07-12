import re
regex=re.compile(r'^[A-Z]+[0-9]{2}+[@|#|$|%|^|&|*{2}]{7,15}')
int=input()
ex=regex.findall(int)
h=ex.group()
print(h)