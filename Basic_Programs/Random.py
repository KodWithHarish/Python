import random
def getRoll(RollNo):
    if RollNo == 1:
        return 'Abhijeet'
    elif RollNo == 2:
        return 'Adarsh'
    elif RollNo == 3:
        return 'Darshan'
    elif RollNo == 4:
        return 'Karthik'
    elif RollNo == 5:
        return 'Devendra'
    elif RollNo == 6:
        return 'Shreeshail'
    elif RollNo == 7:
        return 'Prajwal'
    elif RollNo == 8:
        return 'Preetam'
    else:
        return 'Harish'
  

r = random.randint(1,9)
f = getRoll(r)
print(f)

