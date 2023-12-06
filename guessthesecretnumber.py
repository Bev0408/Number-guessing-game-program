import random
# welcomes user and explains the game explain the game to user
print("Welcome to the number guessing game! Keep attempting to guess the secret number until you get it right")
secret_number = random.randint(1,100)
#loops until user guesses correctly
while True:
    try:
        # get users guess
        users_guess = int(input("please enter you guess: "))

        if users_guess > secret_number:
            print("incorrect,try again and go lower!")
        elif users_guess < secret_number:
            print("incorrect, try agian and go higher!")
        else:
            print("Congratulations! You guessed the secret number.")
            break
    except ValueError:
        print("please enter a number!")
