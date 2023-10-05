#tictactoe
import pyfiglet

sign_list = []

for i in range(9):
  sign_list.append(' ')


def print_board(sign_list):
    board = f"""

    {sign_list[0]} | {sign_list[1]} | {sign_list[2]}
   ---|---|---
    {sign_list[3]} | {sign_list[4]} | {sign_list[5]}
   ---|---|---
    {sign_list[6]} | {sign_list[7]} | {sign_list[8]}

  """
    print(board)


index_list = []
def take_input(player_name):
  while True:
    x = int(input(f'{player_name}: '))
    x -= 1
    if 0 <= x < 10:
      if x in index_list:
        print('This spot is blocked.')
        continue
      index_list.append(x)  
      return x
    print('Please Enter number between 1-9')

    
def check_win(sign_list, player_one, player_two):
    if sign_list[0] == sign_list[1] == sign_list[2] == 'X' or sign_list[1] == sign_list[4] == sign_list[7] == 'X' or sign_list[0] == sign_list[4] == sign_list[8] == 'X' or sign_list[2] == sign_list[5] == sign_list[8] == 'X' or sign_list[3] == sign_list[4] == sign_list[5] == 'X' or sign_list[2] == sign_list[4] == sign_list[6] == 'X' or sign_list[6] == sign_list[7] == sign_list[8] == 'X' or sign_list[0] == sign_list[3] == sign_list[6] == 'X' :
        print(f'Congratulations {player_one}. You WON.!!')
        quit('Thank you both for joining')
        playgame = False    
    elif sign_list[0] == sign_list[1] == sign_list[2] == 'O' or sign_list[1] == sign_list[4] == sign_list[7] == 'O' or sign_list[0] == sign_list[4] == sign_list[8] == 'O' or sign_list[2] == sign_list[5] == sign_list[8] == 'O' or sign_list[3] == sign_list[4] == sign_list[5] == 'O' or sign_list[2] == sign_list[4] == sign_list[6] == 'O' or sign_list[6] == sign_list[7] == sign_list[8] == 'O' or sign_list[0] == sign_list[3] == sign_list[6] == 'O' :
        print(f'Congratulations {player_two}. You WON.!!')
        quit('Thank you both for joining')
    
def start_game():
      playgame = True
      current_turn = 1
      player_one = input("Enter player 1 name: ")
      player_two = input("Enter player 2 name: ")
      print_board(sign_list)
      while(playgame):
        if current_turn == 1:
            index = take_input(player_one)
            sign_list[index] = 'X'
        else:
            index = take_input(player_two)
            sign_list[index] = 'O'
        current_turn = 3 - current_turn
        print_board(sign_list)
        check_win(sign_list, player_one, player_two)






def display_menu():
    banner = pyfiglet.figlet_format("TicTacToe")
    print(banner)
    print("Welcome to the TicTacToe Game!")
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
        print("Starting Game...")
        start_game()
    elif menu_user_choice == "2":
        # Display instructions
        print(f''' 
    Instructions:

     1 | 2 | 3  
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9  

    1.Numbers represent position where input will fill 

    2.Each player can guess once at a time

    3.All spots should be filled for someone to win the game
              ''')
        input("Press Enter to continue...")
    elif menu_user_choice == "3":
        # Quit the game
        print("Goodbye!")
        break
