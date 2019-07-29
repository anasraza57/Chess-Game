from GameBoard import GameBoard
from sys import exit

# display_ins()
n = input("Press Y to Start the Game and N for Cancel: ")
while n != 'y' and n != 'Y' and n != 'n' and n != 'N':
    n = input("Please Enter Y/N:  ")
else:
    if n == 'y' or n == 'Y':
        print("\n\033[1;35;48m Here's the Board. Let's Play Baby!\033[0;37;48m\n\n")
        gb = GameBoard()
        gb.display_board(gb.arr)
    else:
        exit()
