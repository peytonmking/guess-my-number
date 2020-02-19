import random

cont = "y"
guess = 0
answer = 0.1
guesses = 0

while cont == "y":

    lower_num = int(input("Enter the lower range for the computer to generate: "))
    upper_num = int(input("Enter the upper range for the computer to generate: "))

    answer = random.randint(lower_num,upper_num)

    print(f"Number generated between {lower_num} and {upper_num}.")

    while guess != answer:

        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess > answer:
            print("Too high!")

        elif guess < answer:
            print("Too low!")

        else:
            print(f"You guessed it! That took you {guesses} guesses!")
            guesses = 0

    answer = 0.1

    cont = input("Enter y to play again, if not enter anything else.")



