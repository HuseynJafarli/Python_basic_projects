import pyfiglet

def initialize_board():
    return [" " for _ in range(9)]

def print_board(sign_list):
    board = f'''
      {sign_list[0]} | {sign_list[1]} | {sign_list[2]}
     ---|---|---
      {sign_list[3]} | {sign_list[4]} | {sign_list[5]}
     ---|---|---
      {sign_list[6]} | {sign_list[7]} | {sign_list[8]}
    '''
    print(board)

def take_input(player_name):
    while True:
        try:
            x = int(input(f"{player_name}: ")) - 1
            if 0 <= x < 9:
                return x
            else:
                print("Please enter a number between 1 and 9")
        except ValueError:
            print("Invalid input. Please select an integer between 1 and 9")

def check_win(sign_list, player_name):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

    for combo in win_combinations:
        a, b, c = combo
        if sign_list[a] == sign_list[b] == sign_list[c] != " ":
            print(f"Congratulations {player_name}. You WON!!")
            return True
    
    return False

def is_board_full(sign_list):
    return " " not in sign_list

def play_again():
    return input("Do you want to play again? (Y/N): ").strip().lower() == "y"

def start_game():
    while True:
        player_one = input("Enter player 1 name: ")
        player_two = input("Enter player 2 name: ")
        players = [player_one, player_two]
        signs = ["X", "O"]
        current_player = 0
        sign_list = initialize_board()

        while True:
            print_board(sign_list)
            index = take_input(players[current_player])

            if sign_list[index] == " ":
                sign_list[index] = signs[current_player]
            else:
                print("This spot is already occupied. Try again.")
                continue

            if check_win(sign_list, players[current_player]):
                print_board(sign_list)
                break

            if is_board_full(sign_list):
                print("It's a tie! The game is over.")
                break

            current_player = 1 - current_player

        if not play_again():
            print("Goodbye!")
            break

def display_menu():
    banner = pyfiglet.figlet_format("TicTacToe")
    print(banner)
    print("Welcome to TicTacToe!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")

def get_menu_choice():
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

while True:
    display_menu()
    menu_user_choice = get_menu_choice()
    
    if menu_user_choice == "1":
        print("Starting Game...")
        start_game()
    elif menu_user_choice == "2":
        print(''' 
    Instructions:

     1 | 2 | 3  
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9  

    1. Numbers represent positions where input will fill.

    2. Each player can guess once at a time.

    3. The game ends when a player wins or it's a tie (all spots are filled).
              ''')
        input("Press Enter to continue...")
    elif menu_user_choice == "3":
        print("Goodbye!")
        break
