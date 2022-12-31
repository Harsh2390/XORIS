import random
import os

XSIZE = 15
YSIZE = 15
# for extra number of player
Num_Players = 5
#Num_Players = 2
Players = ["X", "O", "R", "I", "S"]
#Players = ["X", "O"] 
# Randomly selecting the first player
first_turn = random.randint(0,Num_Players - 1)


Board = []

# creating our matrix for game
for row in range(XSIZE):
    row_list1 = []
    for col in range(YSIZE):
        row_list1.append(' ')
    Board.append(row_list1)

# this function will print the board
def print_board():
    print("\t", end='')
    for col in range(YSIZE):
        print("   " + chr(65 + col), end='')


    print("\n\t +" + "---+" * YSIZE)

    for row in range(XSIZE):
        print(str(row) + '\t |', end=" ")
        for col in range(YSIZE):
            print(Board[row][col] + ' | ', end="")
        print("\n\t +"+"---+"*YSIZE)
# this function will check all the possibility for wining
def winning_move(Board, Player):
    # checking for win in horizontal combination
    for c in range(YSIZE - 3):
        for r in range(XSIZE):
            if Board[r][c] == Player and Board[r][c+1] == Player and Board[r][c+2] == Player and Board[r][c+3] == Player:
                return True
    # checking for win in vertical combination
    for c in range(YSIZE):
        for r in range(XSIZE - 3):
            if Board[r][c] == Player and Board[r+1][c] == Player and Board[r+2][c] == Player and Board[r+3][c] == Player:
                return True

    # checking for win in ascending slope
    for c in range(YSIZE-3):
        for r in range(XSIZE - 3):
            if Board[r][c] == Player and Board[r+1][c+1] == Player and Board[r+2][c+2] == Player and Board[r+3][c+3] == Player:
                return True
    
    # checking for win in descending slope
    for c in range(YSIZE-3):
        for r in range(3, XSIZE):
            if Board[r][c] == Player and Board[r-1][c+1] == Player and Board[r-2][c+2] == Player and Board[r-3][c+3] == Player:
                return True
# this function will check for the draw 
# this function will check all the elements of nested list and 
# if every element is filled with other than " "(empty space) then it will return true
def draw_check(Board):
    return not any(" " in a for a in Board)



wins = False

print_board()

# initializing the game 

while wins == False:

    # first randomly accessing our player form our player's list 
    turn_index = first_turn
    Player = Players[turn_index]
    # now this piece of code will access the just next player after first player
    # and when we reach at the end of player's list then it will restart accessing the players from start
    if turn_index == Num_Players -1:
        first_turn = 0
    else:
        first_turn = first_turn + 1


    # asking for the input
     
    players_input = list(input(Player + "'s turn please enter the coordinates in the form of 'A7, B5, C6 to place the checker: "))

    # if our input is over one digit last no. for ex = 13, 15, 10 etc
    # if our input is less than 2 then assign it -1 so that it get process in next while loop to get valid input to process


    if len(players_input) >= 3 and players_input[1].isdigit() and players_input[2].isdigit():
        temp_guess_row = (players_input[1]+players_input[2])
        check_guess_row = int(temp_guess_row)
        check_guess_col = (ord(players_input[0])-65)
    elif len(players_input) == 2 and players_input[1].isdigit():
        temp_guess_row = (players_input[1])
        check_guess_row = int(temp_guess_row)
        check_guess_col = (ord(players_input[0])-65)
    else:
        temp_guess_col = -1
        temp_guess_row = -1
        check_guess_row = int(temp_guess_row)
        check_guess_col = int(temp_guess_col)


    # checking for valid input
    # weather first first element of our Alphabet or not and second element is a no. or not
    # then checking for the range of our input, weather its a within the scope of board or not
    # if length of input is less than 1 or o then ask for input again

    while (len(players_input) <= 1 or players_input[0].isdigit()) == True or (players_input[1].isdigit()) == False or\
            ord(players_input[0])-65 > XSIZE or ord(players_input[0])-65 < 0 or int(temp_guess_row) > YSIZE\
            or check_guess_col < 0 or check_guess_col >= YSIZE\
        or check_guess_row < 0 or check_guess_row >= XSIZE or int(temp_guess_row) < 0 or Board[check_guess_row][check_guess_col] != " ":
        players_input = list(input(Player +" 's turn Please enter the coordinates again in correct format like A6, B2, C9 etc. and within the range : "))


        # here we are checking our input weather its within range of valid inputs like only A is invalid if A13 then then separating "A" and "13"
        # and checking our third digit of input is a number or not like A3A is invalid so need the input again

        if len(players_input) >= 3 and players_input[1].isdigit() and players_input[2].isdigit():
            temp_guess_row = (players_input[1]+players_input[2])
            check_guess_row = int(temp_guess_row)
            check_guess_col = (ord(players_input[0])-65)
        elif len(players_input) == 2 and players_input[1].isdigit():
            temp_guess_row = (players_input[1])
            check_guess_row = int(temp_guess_row)
            check_guess_col = (ord(players_input[0])-65)
        else:
            temp_guess_col = -1
            temp_guess_row = -1
            check_guess_row = int(temp_guess_row)
            check_guess_col = int(temp_guess_col)

    # now this condition help to process higher digit inputs like A11 or A54
    if len(players_input) >= 3:
        comb_no = players_input[1]+players_input[2]
        guess_row = int(comb_no)
    else:
        guess_row = int(players_input[1])

    guess_col = (ord(players_input[0])-65)


    Board[guess_row][guess_col] = Player

    os.system("clear")
    #os.system('cls')
    print_board()
    

# now this if condition will check who won the game using winning move function defined above
    if winning_move(Board, Player):
        print(Player + " win the game")
        wins = True
# this if condition will check weather the game is over or not with draw
    if draw_check(Board):
        print("Game is draw ")
        wins = True


    

    






