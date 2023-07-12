string = 'Harish Kumbhar from Manakapur'
vowels = 0
consonent = 0
dict = {}

for c in string:
    if c in dict:
        dict[c] += 1
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        vowels = vowels + 1
    else:
        dict[c] = 1
        consonent = consonent + 1 

    

print(str(dict)) 
print('No. of vowels in given string : '+str(vowels)) 
print('No. of consonents in given string : '+str(consonent))  


