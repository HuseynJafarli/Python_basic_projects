import random

def play_game():
    num = random.randint(1, 100)
    attempts = 0
    previous_guesses = set()

    print("Welcome to the Advanced Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it.")

    while True:
        guess = input("Take a guess: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts += 1

        if guess == num:
            print(f"Congratulations! You guessed the number {num} in {attempts} attempts.")
            break
        elif guess in previous_guesses:
            print("You've already guessed that number. Try a different one.")
        else:
            previous_guesses.add(guess)
            if guess < num:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

    return attempts

def main():
    previous_score = None

    while True:
        attempts = play_game()

        if previous_score is not None:
            print(f"Previous Score: {previous_score} attempts")

        play_again = input("Do you want to play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            print("Goodbye!")
            break

        previous_score = attempts

if __name__ == "__main__":
    main()