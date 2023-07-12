import random

def guess(x):
    randomNo = random.randint(1,x)
    guess = 0
    while guess != randomNo:
        guess = input(f'Guess the No b/w 1 & {x}: ')
        print(guess)
    
guess(10)
