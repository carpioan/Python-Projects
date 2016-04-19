import random

board = []

for x in range(4):
    board.append([" "] * 3)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Hai sa jucam X si O!"
print_board(board)


""""for turn in range(50):
    print "Turn", turn + 1"""
	
comp_row = random.randint(1, 3)
comp_col = random.randint(1, 3)
print comp_row
print comp_col
board[comp_row][comp_col] = "O"
print print_board(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
""""for turn in range(50):
    print "Turn", turn + 1
	guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
	board[random_row][random_col] = "O"
	board[guess_row][guess_col] = "X"
    
	print print_board(board)"""