import pyfiglet

col = [[] , [] , [] , [] , [] , [] , []]
for i in range(7):
    for j in col:
        j.append(" ")
    

def print_board():
    for row in range(6):
        for i in range(7):
            print("[" + col[row][i] + "]", end="")
        print()
    print()
            
            
            
def take_input(current_turn):
    pass

def check_win():
    pass


def start_game():
    current_turn = 1 
    playgame = True
    signs = ["X","O"]
    print_board()
  
    
    
    

    
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
