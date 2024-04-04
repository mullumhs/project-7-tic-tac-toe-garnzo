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
        board.append(["-","-","-","-","-","-","-",])
    print_board()

def print_board():
    print("1 2 3 4 5 6 7")
    for row in board:
        print()
        print(row, end= "")
    for collum in row:
        print("-")

    
start()