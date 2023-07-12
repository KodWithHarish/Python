num = int(input('Enter A Number\n'))
flag = False
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print('It is not a prime number\n')
    else:
        print('It is a prime number\n')