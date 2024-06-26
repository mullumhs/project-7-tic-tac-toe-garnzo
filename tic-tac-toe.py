# lists
board = []

# welcome
def main():
    playerCount = 1
    welcome()
    menu()
    while True:
        print_board()
        playerCount = tokenplace(playerCount)
        if win_check():
            if playerCount % 2 == 0:
                print("Player O has won")
            else:
                print("Player X has won")
            break
            

    

def welcome():
    print("***********")
    print("Tic Tac Toe")
    print("***********")
    print("")
    redirect = input("Press Enter to show menu: ")
    

# functions
def menu():
    print("Press 1 to show welcome screen")
    print("Press 2 to Start Game")
    print("Press 3 to Quit")
    print("")
    redirect = int(input("Select Option: "))
    if redirect == 1:
        welcome()
    elif redirect == 2:
        initilise_board()
    else:
        return

def initilise_board():
    for row in range(3):
        board.append(["-","-","-",])

def print_board():
    print(" 1 2 3")
    for row in board:
        print()
        for collum in row:
            print(collum, end= "|")

def tokenplace(playerCount):
    token = "X"
    if playerCount % 2 == 0:
        token = "O"

    print()
    update = 0
    while not update == 1:
        # user input
        colluminp = int(input("Enter collum (1-3): ")) - 1
        rowinp = int(input("Enter Row (1-3): ")) -1

        # input validation
        if colluminp >= 0 and colluminp <= 2 and rowinp >= 0 and rowinp <= 2:
                # token place
                if board[rowinp][colluminp] == "-":
                    board[rowinp][colluminp] = token
                    playerCount += 1
                    update = 1
                else:
                    print("Token already has X/O in it, Try Again")          
        else:
            print("Error, number is not in Range 1-3, Try Again")   
        
    return playerCount

def win_check():
    if win_check_hori() or win_check_verti() or win_check_diagy():
        return True
        
    
def win_check_hori():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and not board[i][0] == "-":
            return True
           

def win_check_verti():
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and not board[0][i] == "-":
        
            return True
                

def win_check_diagy():
    return False
    
# call
main()
