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
    colluminp = int(input("Enter collum (1-3): ")) - 1
    for row in range(2, -1, -1):
        if board[row][colluminp] == "-":
            board[row][colluminp] = token
            playerCount += 1
            return playerCount

# call
main()
