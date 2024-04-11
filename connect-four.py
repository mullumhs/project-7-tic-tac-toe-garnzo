board = []

def main():
    playerCount = 1
    start()
    initilise_board()
    while True:
        print_board()
        playerCount = tokenplace(playerCount)
        wincheckhori()

def start():
    print("*********")
    print("Connect 4")
    print("*********")
    print("")
    input("Press enter to play!")
    
def initilise_board():
    for row in range(6):
        board.append(["-","-","-","-","-","-","-",])
    
def print_board():
    print(" 1 2 3 4 5 6 7")
    for row in board:
        print()
        for collum in row:
            print(collum, end= "|")
        
def tokenplace(playerCount):
    token = "X"
    if playerCount % 2 == 0:
        token = "O"

    print()
    colluminp = int(input("Enter collum (1-7): ")) - 1
    for row in range(5, -1, -1):
        if board[row][colluminp] == "-":
            board[row][colluminp] = token
            playerCount += 1
            return playerCount
     
def wincheckhori():
    for row in range(6):
        for col in range(4):
            board[row][col] = board[row][col + 1] = board[row][col + 2] = board[row][col + 3]
        
main()