import random
import time
import keyboard
import os

min_num = int(input('Min: '))
max_num = int(input('Max: '))
set = int(input('do 1 if pick random 2 if you pick: '))
numtog = random.randint(min_num, max_num)
if set == 2:
    numtog = int(input('what number chat: '))
elif set == 1:
    print('alr gng')
    pass
print(f'The number to guess is: {numtog}')
time.sleep(1)
low = min_num
high = max_num
attempts = 0
while True:
    guess = (low + high) // 2
    print(guess)
    attempts += 1

    if guess == numtog:
        print(f'{numtog} is the number, after {attempts} attempts!')
        break
    elif guess > numtog:
        high = guess - 1
    else:
        low = guess + 1
print('Press space to continue')
keyboard.wait('space')
os.exit()