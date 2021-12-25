from print_board import *
from random import randrange
from functools import partial
text = partial(print, sep='', end="\n\n")

def play(board, turn, u_icon, b_icon, round, bot):

    choice = ''

    print_board(board, round)

    if turn == "user":

        good = False
        while not good:
            good = True
            text(bot,": Your turn! Which place (0-8) would you like to play?")
            choice = input("--> ")
            if choice not in board or (choice == 'X' or choice == 'O' or not choice):
                text(bot,": That's not an option, sorry.")
                good = False

        board[board.index(choice)] = u_icon
            
    else:
        
        while choice not in board: # while choice is not an option
            choice = str(randrange(0,8)) # generate choice (0-8)
        text(bot,": My turn! I'll pick... ",choice,"!")

        board[board.index(choice)] = b_icon

    return check_for_win(board)

def check_for_win(board):

    # check for horizontal win
    i = 0
    while i < 9: # look through rows 0-2, 3-5, and 6-8
        if board[i] == board[i + 1] and board[i] == board[i + 2]:
            return board[i]
        i += 3

    # check for vertical win
    i = 0
    while i < 3: # look through columns 0;3;6, 1;4;7, and 2;5;8
        if board[i] == board[i + 3] and board[i] == board[i + 6]:
            return board[i]
        i += 1

    # check for diagonal win
    if board[0] == board[4] and board[0] == board[8]:
        return board[0]
    elif board[2] == board[4] and board[2] == board[6]:
        return board[2]

    for b in board:
        if b is not 'X' and b is not 'O':
            return '' # return blank if no winner yet and there are still open spaces

    return 'C' # return C if no winner yet and there are NOT still open spaces