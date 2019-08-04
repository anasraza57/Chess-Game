from GameBoard import GameBoard
from sys import exit
from Player1 import Player1

# display_ins()
n = input("Press Y to Start the Game and N for Cancel: ")
while n != 'y' and n != 'Y' and n != 'n' and n != 'N':
    n = input("Please Enter Y/N:  ")
else:
    if n == 'y' or n == 'Y':
        print("\n\033[1;35;48m Here's the Board. Let's Play Baby!\033[0;37;48m\n\n")
        gb = GameBoard()
        while True:
            p1 = Player1(gb.arr)
            gb.display_board(gb.arr)
            p1.p1_pawn_mov()
    else:
        exit()
