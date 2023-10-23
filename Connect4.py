import pyfiglet

def reset_board():
    global col 
    col = [[" " for _ in range(7)] for _ in range(6)]


def print_board():
    for row in range(6):
        for i in range(7):
            print("[" + col[row][i] + "]", end="")
        print()
    print()
            
                  
def take_input(current_turn):
     while True:
        try:
            x = int(input(f"Player {current_turn}: "))
            if 0 < x < 8:
                return x
            else:
                print("Please enter a number between 1 and 7")
        except ValueError:
            print("Invalid input. Please select an integer between 1 and 7")

def check_win(current_turn , sign):
    for row in range(6):
        for col_start in range(4):
            if (
                col[row][col_start] == col[row][col_start + 1] == col[row][col_start + 2] == col[row][col_start + 3] == sign
            ):
                return f"Player {current_turn} wins!"

    # Check for a win in columns
    for col_index in range(7):
        for row_start in range(3):
            if (
                col[row_start][col_index] == col[row_start + 1][col_index] == col[row_start + 2][col_index] == col[row_start + 3][col_index] == sign
            ):
                return f"Player {current_turn} wins!"

    # Check for a win in diagonals (top-left to bottom-right)
    for row_start in range(3):
        for col_start in range(4):
            if (
                col[row_start][col_start] == col[row_start + 1][col_start + 1] == col[row_start + 2][col_start + 2] == col[row_start + 3][col_start + 3] == sign
            ):
                return f"Player {current_turn} wins!"

    # Check for a win in diagonals (bottom-left to top-right)
    for row_start in range(3, 6):
        for col_start in range(4):
            if (
                col[row_start][col_start] == col[row_start - 1][col_start + 1] == col[row_start - 2][col_start + 2] == col[row_start - 3][col_start + 3] == sign
            ):
                return f"Player {current_turn} wins!"

    # Check for a tie (board is full)
    if all(col[row][col_index] != " " for row in range(6) for col_index in range(7)):
        return "It's a tie!"

    return None        

def start_game():
    reset_board()
    current_turn = 1 
    sign = " "
    playgame = True
    print_board()
    while playgame:
        if current_turn == 1:
            sign = "X"
        else:
            sign = "O"
        index = take_input(current_turn) - 1
        
        # Check for available space in the chosen column
        for r in range(6, 0, -1):
            if col[r-1][index] == " ":
                col[r-1][index] = sign
                break
        else:
            # If the loop completes without a break, the column is full
            print("This column is already full. Please choose another column.")
            continue  
        
        print_board()
        if check_win(current_turn , sign) is not None:
            print(check_win(current_turn , sign))
            play_again = input("Play again? Y/N:").lower()
            if play_again == "y":
                start_game()
            else:
                playgame = False
        current_turn = 3 - current_turn
        
def display_menu():
    banner = pyfiglet.figlet_format("Connect 4" , font = "slant")
    print(banner)
    print("Welcome to Connect4!")
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

         [ ][ ][ ][ ][ ][ ][ ]            
         [ ][ ][ ][ ][ ][ ][ ]
         [ ][ ][ ][ ][ ][ ][ ]
         [ ][ ][ ][ ][ ][ ][ ]
         [ ][ ][ ][ ][ ][ ][ ]
         [ ][ ][ ][ ][ ][ ][ ]
          1  2  3  4  5  6  7
     

    1. Numbers at the bottom represent position where input will fill.

    2. Each player can guess once at a time.
    
    3. Inputs fill the gaps from bottom to top 
    
    4. Player wins when 4 places in rows of columns filled with the same sign.

    5. The game ends when a player wins or it's a tie (all spots are filled).
              ''')
        input("Press Enter to continue...")
    elif menu_user_choice == "3":
        print("Goodbye!")
        break
