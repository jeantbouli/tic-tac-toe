    # Drawing the board on the console and using the \n command to move to the next line
    # Giving our function an input of spots
    # Mapping the keys into the board
def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def check_turn(turn):
    #We use the modulo operator to find out if the turn is even or odd and dub each turn with it's relative symbol
    if turn % 2 == 0: return "O"
    else: return "X"
#We need to determine if a player has won, and there are 8 such cases , 2 diagnoally, 3 vertically, 3 horizontally 
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
    
    else: return False