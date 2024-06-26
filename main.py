from helpers import draw_board, check_turn, check_for_win
import os

# Dictionary to store the spots on the board with unique identifiers
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

# Game loop to keep the game running until completion
playing = True
complete = False

# Variable to track the player's turn
turn = 0
prev_turn = -1

while playing:
    os.system("cls" if os.name == "nt" else "clear")
    draw_board(spots)

    # Prompting the player for their turn
    if prev_turn == turn:
        print("Invalid Spot Selected, Please Pick Another")
    prev_turn = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit")

    choice = input()

    if choice == "q":
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        # Logic for updating the board with player's choice
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_for_win(spots):
        playing, complete = False, True

    # Checking for a tie
    if turn > 8:
        playing = False

# End of game, displaying results
os.system("cls" if os.name == "nt" else "clear")
draw_board(spots)

if complete:
    # Determining the winner or a tie
    if check_turn(turn) == "X":
        print("Player 1 IS THE WINNER")
    else:
        print("Player 2 IS THE WINNER")
else:
    print("YOU TIED")

print("THANK YOU FOR PARTICIPATING")