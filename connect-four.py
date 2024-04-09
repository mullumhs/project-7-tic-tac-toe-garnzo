board = []

def start():
    print("*********")
    print("Connect 4")
    print("*********")
    print("")
    input("Press enter to play!")
    initilise_board()

def initilise_board():
    for row in range(7):
        board.append(["|-","-","-","-","-","-","-",])
    print_board()

def print_board():
    print(" 1 2 3 4 5 6 7")
    for row in board:
        print()
        for collum in row:
            print(collum, end= "|")

def tokenplace():
    playerCount = 1
    while True:
        token = "X"
        if playerCount % 2 == 0:
            token = "O"

        collum = int(input(f"Enter collum (1-7): " - 1))
        for col in range(6):
            for row in col:
                if board[col][collum] == "-":
                    board[col][collum] == token
                    playerCount += 1
                    break


    
start()