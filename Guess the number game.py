import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("Too high! Try a lower number.\n")
            else:
                print(f"Congratulations! You guessed the number correctly.")
                print(f"It took you {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.\n")


guessing_game()
