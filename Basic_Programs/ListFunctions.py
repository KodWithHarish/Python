# list of integers
listofintergers = [1,2,3,4,5]
print(listofintergers)
print(listofintergers[2])
print('\n')

# list of strings
listofstrings = ['apple','mango','orange']
print(listofstrings)
print(listofstrings[0])
print('\n')

# list of datatypes
listofdatatypes = ['09','harish','true','95.5']
print(listofdatatypes)
print('\n')

# list functions
list = [8,9,1,4,3,5,2,10,6]
print(list)

list.insert(2 ,7)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

list.append('harish')
print(list)

list.extend('kumbhar')
print(list)

list.remove('harish')
print(list)

print(list.index(6))
print(list.index(9,0,4))
print('\n')

# list inside the list
listinsidethelist = ['harish','kumbhar',[1,2,3,4,5]]
print(listinsidethelist)
print(listinsidethelist[0][2])
print(listinsidethelist[2])
print(listinsidethelist[2][2])

listinsidethelist = ['harish','kumbhar',[1,2,[6,7,8,9],3,4,5]]
print(listinsidethelist[2][2][3])