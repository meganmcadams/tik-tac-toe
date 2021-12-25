# includes

import sys
PYTHONPATH = ('<project directory>')

from print_board import *
from play import *
from load import *
from save import *

from functools import partial
text = partial(print, sep='', end="\n\n")

# main

saves = load()

board = ['0','1','2','3','4','5','6','7','8']
bot = "Vay"

text(bot,": Hi! My name is ",bot,". What's your name?")
user = input("--> ")

if user == bot: # if user picks the bot's name
    text(bot,": Oh! We have the same name! That's gonna be a bit confusing.")

try: # check if they've played previously
    u_info = saves[user]
    if int(u_info[0]) > int(u_info[1]): # if wins is more than losses
        text(bot,": Nice to see you again, ",user,"! I'm sure to win this time!")
    else:
        text(bot,": I see you've come back to try to redeem yourself, ",user,". I will win again!")
except KeyError:
    text(bot,": Nice to meet you, ",user,". Let's play some Tic Tak Toe!")

# get user choice for who should go first
text(bot,": Would you like to go first?")
print("  | Y: Yes")
print("  | N: No")
choice = input("--> ")

if choice == 'Y':
    turn = "user"
    text(bot,": Okay, you can go first.")
else:
    turn = "bot"
    text(bot,": Okay, I guess I'll go first then.")
    
# get user choice for being x's or o's
text(bot,": Would you like to be X's or O's?")
print("  | O: O's")
print("  | X: X's")
choice = input("--> ")

if choice == 'O':
    u_icon = "O"
    b_icon = "X"
    text(bot,": Alright! I'll be X's then.")
else:
    u_icon = "X"
    b_icon = "O"
    text(bot,": I guess I'll be O's.")

result = ''
round = 1

while result == '': # play while there isn't a winner

    result = play(board,turn,u_icon,b_icon, round, bot)
    if turn == "bot":
        turn = "user"
    else:
        turn = "bot"
    round += 1

print_board(board, round)

if result == u_icon:
    text(bot,": You won! Congrats!")
elif result == b_icon:
    text(bot,": Ha! I won!")
else:
    text(bot,": Huh... I guess we tied.")

text(bot,": Thanks for playing, ",user,"!")

save(user, result, u_icon, saves)