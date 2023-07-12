# task print no of character in a file with & without spaces & \n character
try:
    with open("file.txt") as file:
         data = file.read()
         print(len(data))
         list = data.split()
         print(len(list))
         countwords = 0
         for word in list:
             countwords += len(word)
         print(countwords)
         # print(sum(len(word)for word in list))

except Exception as e:
    print(e)

# repeated string in file
from collections import Counter
try:
    with open("file.txt") as file:
        data = file.read()
        wordlist = data.split()
        print(Counter(wordlist))

except Exception as e:
    print(e)
