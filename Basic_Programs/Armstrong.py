num = int(input('Enter A Number\n'))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit **3
    temp = temp // 10

if num == sum:
    print('It Is Armstrong\n')
else:
    print('It is not Armstrong\n')