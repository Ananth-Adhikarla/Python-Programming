from random import randint

#initializing board
board = []


for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    
    for row in board:
        print(*row, sep=' ')

#starting the game and printing the board
print ("Let's play Battleship!")
print_board(board)

#defining where the ship is
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#asking the user for a guess
for turn in range(10):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    # if the user's right, the game ends
    if (guess_row == ship_row and guess_col == ship_col):
        print ("Congratulations! You sunk my battleship!")
        break
	
    else:
        #warning if the guess is out of the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Your choice is not in the range of the board.")
        
        #warning if the guess was already made
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")	
        
        #if the guess is wrong, mark the point with an X and start again
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        
        # Print turn and board again here
        print ("Turn " + str(turn+1) + " out of 10.") 
        print_board(board)

#if the user have made 10 tries, it's game over

if(turn >= 9):
	print("\n")
	print("Game Over")
	print("The BattleShip was located at row : " , ship_row , " at col : " , ship_col)
 

