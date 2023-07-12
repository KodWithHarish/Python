year = int(input("Enter Year\n"))
if (year % 400 == 0):
        print(str(year)+" Is A Leap Year\n")
elif (year % 100 == 0):
        print(str(year)+" Is Not A Leap Year\n")
elif (year % 4 == 0):
        print(str(year)+" Is A Leap Year\n")
else:
        print(str(year)+" Is Not A Leap Year\n")