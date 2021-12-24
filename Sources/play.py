from print_board import *
#from functools import partial
#text = partial(print, sep='', end="\n\n")

def play(board, turn, u_icon, b_icon, round, bot):

    result = ''

    print_board(board, round)

    if turn == "user":
 #       text(bot,": Which place (0-8) would you like to play?")
        print("text")
    else:
        print("bot")

    return result