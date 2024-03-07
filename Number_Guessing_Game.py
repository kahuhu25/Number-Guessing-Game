import random

def number_guessing_game():
    print("Hello! Welcome to Number Guessing Game")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Let's start the game!")

    # Set the number of attempts
    attempts = 0

    while attempts < 10:
        try:
            # Prompt the player to guess the number
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You have guessed the correct number.")
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    secret_number = random.randint(1, 100)
                    attempts = 0
                    print("Let's play again!")
                else:
                    print("Thank you for playing!")
                    break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == 10:
        print("Sorry, you've run out of attempts. The correct number was {}.".format(secret_number))

if __name__ == "__main__":
    number_guessing_game()
