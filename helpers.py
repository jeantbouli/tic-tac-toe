# Drawing the board on the console and using the \n command to move to the next line
# Function to draw the Tic-Tac-Toe board based on the spots
def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

# Function to determine whose turn it is (X or O) based on the turn number
def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

# Function to check if a player has won by examining the spots on the board
def check_for_win(spots):
    if   (spots[1] == spots[2] == spots[3]) \
      or (spots[4] == spots[5] == spots[6]) \
      or (spots[7] == spots[8] == spots[9]):
        return True
    # Handle Vertical Cases
    elif   (spots[1] == spots[4] == spots[7]) \
      or (spots[2] == spots[5] == spots[8]) \
      or (spots[3] == spots[6] == spots[9]):
        return True
    # Diagonal Cases
    elif (spots[1] == spots[5] == spots[9]) \
      or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False