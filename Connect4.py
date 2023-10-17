import pyfiglet

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

def check_win():
    pass


def start_game():
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
            continue  # Go back to the start of the loop
        
        print_board()
        
        current_turn = 3 - current_turn
        if check_win() is not None:
            playgame = False

        
    
    
    

    
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
    
    4. Player wins when 4 places in rows of columns filled.

    5. The game ends when a player wins or it's a tie (all spots are filled).
              ''')
        input("Press Enter to continue...")
    elif menu_user_choice == "3":
        print("Goodbye!")
        break
