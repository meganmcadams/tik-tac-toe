# includes

import sys
PYTHONPATH = ('<project directory>')

from print_board import *
from functools import partial
from play import *
text = partial(print, sep='', end="\n\n")

# main

board = []
bot = "Vay"

i = 0
for i in range(9):
    board.append(i)

text(bot,": Hi! My name is ",bot,". What's your name?")
user = input("--> ")

if user == bot: # if user picks the bot's name
    text(bot,": Oh! We have the same name! That's gonna be a bit confusing.")
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
    print("Test")
    break

text(bot,": Thanks for playing, ",user,"!")