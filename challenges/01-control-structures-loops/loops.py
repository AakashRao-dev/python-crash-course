# =============== While Loop ===============
# Challenge 1: Sum of Natural Numbers
# Write a program to find the sum of the first n natural numbers using a while loop.

# Challenge 2: Guessing Game
# Write a program that generates a random number between 1 and 100, and then lets the user guess the number. The program should continue until the user guesses the correct number, giving feedback if the guess was too high or too low.

# Challenge 3: Multiplication Table
# Create a program that prints the multiplication table of any number provided by the user, using a while loop.

from random import randrange

# 1
n = 1
sum = 0
while n <= 10:
    sum += n
    n += 1
print('The Sum is:', sum)


# 2
random_number = randrange(1, 100)
print(random_number)
guess = int(input('Guess the Number (between 1-100): '))

while guess != random_number:
    if guess > random_number:
        print('Too High!')
    elif guess < random_number:
        print('Too Low!')

    guess = int(input('Guess again: '))

print('Corect Guess :)')

# 3
num = int(input('Enter the number for multiplication table: '))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# ======================================================
