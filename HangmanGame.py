import pyfiglet
import random

def start_game(words_list):
    attempts = 7
    play_game = True
    # List to make sure that player can only choose 1 letter at a time
    choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Creating unknown word by using "_"
    selected_word = random.choice(words_list).lower()
    not_guessed_word = ""
    for c in selected_word:
        not_guessed_word += "_"
        if c == " ":
            space_index = selected_word.index(" ")
            not_guessed_word = not_guessed_word[:space_index] + " " + not_guessed_word[space_index+1:] 
    guessed_word = not_guessed_word
    print(f"You have {attempts} attempts. Start guessing!")
    print(not_guessed_word)
    # Main game logic
    while(play_game):
        user_choice = input("Please enter a letter or a word: ").lower()
        if user_choice in choices: 
            choices.remove(user_choice)
            if user_choice not in selected_word:
                attempts -= 1
                print(f"You have {attempts} attempts left")
            for i in range(len(selected_word)): 
                if selected_word[i] == user_choice:
                    guessed_word = not_guessed_word[:i] + user_choice + not_guessed_word[i+1:]
                    not_guessed_word = guessed_word               
            print(guessed_word)
            # Win / Lose conditions
            if attempts == 0:
                print("You Lose.")
                play_game = False    
            if guessed_word == selected_word:
                play_again = input("You win! Play again? Y/N: ").lower()

                if play_again == "y":
                    start_game(words_list)
                if play_again == "n":
                    play_game = False
                    return 1
        elif user_choice == selected_word:
            not_guessed_word = selected_word
            play_again = input("You win! Play again? Y/N: ")  
            if play_again == "y":
                start_game(words_list)
            if play_again == "n":
                play_game = False
        else:
            print(f"Invalid choice or you already selected {user_choice}. Please select a different letter.")


# Function to display the menu with fancy text
def display_menu():
    banner = pyfiglet.figlet_format("Hangman Game")
    print(banner)
    print("Welcome to the Hangman Game!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")

# Function to handle user input for the menu
def get_menu_choice():
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Main menu loop
while True:
    display_menu()
    menu_user_choice = get_menu_choice()
    
    if menu_user_choice == "1":
        # Select the category and start the game
        def get_category_choice():
            while True:
                category_choice = input("Enter your category choice: IT(1) , Cars(2) , Countries(3) , Animals(4): ")
                if category_choice in ["1", "2", "3" , "4"]:
                    return category_choice
                else:
                    print("Invalid choice. Please choose 1, 2, or 3.")
                    
        category_menu_choice = get_category_choice()
        
        if category_menu_choice == "1":
            words_list = [
            "computer", "programming", "hangman", "python", "developer", "keyboard", "software",
            "internet", "database", "algorithm", "variable", "function", "debugging", "version",
            "code", "project", "repository", "collaboration", "framework", "documentation"
        ]
        elif category_menu_choice == "2":
            words_list = [
            "Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes-Benz", "Volkswagen",
            "Audi", "Hyundai", "Jeep", "Subaru", "Tesla", "Kia", "Ferrari", "Lamborghini", "Porsche",
            "Mitsubishi", "Volvo", "Mazda", "Lexus", "Jaguar", "Chrysler", "Dodge", "Buick",
            "Cadillac", "Land Rover", "Infiniti", "Acura"
        ]
        
        elif category_menu_choice == "3":
            words_list = [
            "United States", "Canada", "United Kingdom", "Australia", "Germany", "France", "Japan",
            "Brazil", "India", "China", "South Africa", "Mexico", "Italy", "Spain", "Russia",
            "South Korea", "Argentina", "Sweden", "New Zealand", "Singapore", "Egypt", "Thailand",
            "Ireland", "Greece", "Turkey", "Netherlands", "Norway", "Denmark", "Finland"
        ]

        elif category_menu_choice == "4":
            words_list = [
            "Lion", "Elephant", "Tiger", "Giraffe", "Cheetah", "Kangaroo", "Dolphin", "Penguin",
            "Gorilla", "Zebra", "Polar Bear", "Koala", "Chimpanzee", "Orangutan", "Panda",
            "Hippopotamus", "Leopard", "Rhinoceros", "Camel", "Gazelle", "Koala", "Peacock",
            "Sloth", "Snake", "Jaguar", "Cheetah", "Squirrel", "Owl", "Puma", "Bear"
        ]
                    
        start_game(words_list)
    elif menu_user_choice == "2":
        # Display instructions
        print("Instructions:")
        print("Guess the word one letter at a time.")
        print("You have a limited number of incorrect guesses.")
        input("Press Enter to continue...")
    elif menu_user_choice == "3":
        # Quit the game
        print("Goodbye!")
        break
