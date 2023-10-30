import random

num = random.randrange(1,11)

guess = int(input('Enter any number between 1 to 10:'))

while num != guess:
    if guess < num:
        print('Too Low')
        guess = int(input('Enter any number between 1 to 10:'))
    elif guess > num:
        print('Too High')
        guess = int(input('Enter any number between 1 to 10:'))
    else:
        break
print('You guessed it right!!')
