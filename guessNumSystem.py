# system generate a random number, and user have to guess it
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number from 1 to {x} : "))
        if guess < random_number:
            print(f"Oops.. Guess higher number!!\n")
        elif guess > random_number:
            print(f"Oops.. Guess lower number!!\n")

    print(f"Yayyyy!!! You guessed it correctly....")

guess(100)