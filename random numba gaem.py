import random
import os
import math
import time
import keyboard
import sys
from pathlib import Path

print('input min')
min = int(input())
print("Input max number")
max = int(input())

num = random.randint(min, max)
print(f'Random number between {min} and {max} has been chosen')
time.sleep(0.5)

won = 0
guessnum = 0

while won == 0:
    print('Choose a number')
    guess = int(input())
    guessnum += 1
    if guess == num:
        print(f'YOU WIN!!! YOU TOOK {guessnum} ATTEMPTS')
        if cheated == 1:
            print('you cheated...')
            time.sleep(1)
            print('Press space to continue...')
            keyboard.wait('space')
        won = 1
        print('Press space to continue...')
        keyboard.wait('space')
        sys.exit
    elif guess == 23482022415:
        print(f'the num is {num} btw')
        guessnum -= 1
        cheated = 1
    elif guess <= min or guess >= max:
        print('Invalid number')
    elif guess < num:
        print(f'The number is higher than {guess}')
    elif guess > num:
        print(f'The number is lower than {guess}')