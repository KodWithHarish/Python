n = int(input("Enter a number\n"))
ln = n % 10
temp = n
while temp >= 10:
    temp //= 10
print("Addition of first and last number is : ",temp+ln)