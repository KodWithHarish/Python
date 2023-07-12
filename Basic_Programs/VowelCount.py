str = input('Enter A String\n')
vowels = 0
Consonent = 0

for c in str :
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        vowels = vowels + 1
    else :
        Consonent = Consonent + 1

print('Number of Vowels in given string : ',vowels)
print('Number of consonents in given string : ',Consonent)

