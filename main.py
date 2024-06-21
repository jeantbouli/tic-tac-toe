from helpers import draw_board,check_turn, check_for_win
#We dont want the board to be redrawn everytime the player inputs a variable
import os 
#we use a dictionary to have a unique identifier that can be used to access or modify data

spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

#Since Games may very in length, with some ending quickly and some lasting as long as possible, the best option for knowing how many times the player needs to update the board is to use a while loop
playing = True
#By defaul, the game isnt won so we set the "Completion" of it to false
complete = False
#If a player enters a number from 1 to 9 we want to put an X or O on that spot, we need to keep track of who's turn it is 
turn = 0
prev_turn = -1
while playing:
    #we use a ternary operator to check what the operating system is to pass the right command and clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    #We begin by drawing the board
    draw_board(spots)
    #Let the player know if an invalid spot is selected 
    if prev_turn == turn:
        print("Invalid Spot Selected, Please Pick Another")
    prev_turn = turn
    print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit")
    #Once the board has been drawn, its time to get input from the player
    choice = input()
    if choice == "q":
        playing = False
    #to check that the input is a number not a letter     and to convert the input to an integer and check if its one of they keys in the spots dictionary
    elif str.isdigit(choice) and int(choice) in spots:
        """we need to solve the issue of overriding a previously reserved spot on the board
        first we're going to want to increment the turn by one and then next we're going to want to pass
        turn into our check turn function which will return either an x or o depending on whose turn it is we're going to
        replace the value of whatever our player gives us the number one through nine on 
        the spot's dictionary with that x or o
        """
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_for_win(spots): playing, complete = False, True
    #Handling Ties1
    if turn > 8: playing = False
    

#Printing the Results, Draw the Board One Last Time
os.system("cls" if os.name == "nt" else "clear")
draw_board(spots)
if complete:
    if check_turn(turn) == "X": print("Player 1 IS THE WINNER")
    else: print("Player 2 IS THE WINNER")
else:
    print("YOU TIED")

print("THANK YOU FOR PARTICIPATING")
