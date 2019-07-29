from numpy import *


class GameBoard:
    def __init__(self):
        self.arr = array([
            ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
            ['0', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ], str)

    @staticmethod
    def display_ins():
        print("\033[1;38;41m READ THE INSTRUCTIONS CAREFULLY \033[0;37;48m")
        print("\033[1;35;48m R = Rook, N = Knight, B = Bishop, K = King, Q = Queen, P = Pawn\033[0;37;48m")
        print("\033[1;35;48m * Upper Case is for player 1 pieces.\033[0;37;48m")
        print("\033[1;35;48m * Lower Case is for player 2 pieces.\033[0;37;48m")
        print("\033[1;35;48m * 0 indicates the empty block.\033[0;37;48m")
        print("\033[1;35;48m * The King is the most important piece, but is one of the weakest. The king can only "
              "move one square in any direction - up, down, to the sides, and diagonally.\n   The king may never move "
              "himself into check (where he could be captured). When the king is attacked by another piece this is "
              "called "'check'".\033[0;37;48m")
        print(
            "\033[1;35;48m * The Queen is the most powerful piece. She can move in any one straight direction - "
            "forward, backward, sideways, or diagonally\n   as far as possible as long as she does not move through "
            "any of her own pieces.\033[0;37;48m")
        print("\033[1;35;48m * The Rook may move as far as it wants, but only forward, backward, and to the sides.\033["
              "0;37;48m")
        print("\033[1;35;48m * Knights move in a very different way from the other pieces – going two squares in one "
              "direction, and then one more move at a 90 degree angle,\n   just like the shape of an “L”. Knights are "
              "also the only pieces that can move over other pieces.\033[0;37;48m")
        print("\033[1;35;48m * The bishop may move as far as it wants, but only diagonally. Each bishop starts on one "
              "color (light or dark) and must always stay on that color.\033[0;37;48m")
        print("\033[1;35;48m * Pawns are unusual because they move and capture in different ways: they move forward, "
              "but capture diagonally. Pawns can only move forward one square at a time,\n   except for their very "
              "first move where they can move forward two squares. Pawns can only capture one square diagonally in "
              "front of them.\n   They can never move or capture backwards. If there is another piece directly in "
              "front of a pawn he cannot move past or capture that piece.\033[0;37;48m\n")

    def display_board(self, pieces):
        for i in range(len(pieces)):
            for piece in self.arr[i]:
                if piece == '0':
                    print("\033[1;37;48m  " + piece, end="")
                elif piece == 'P' or piece == 'R' or piece == 'N' or piece == 'B' or piece == 'Q':
                    print("\033[1;34;48m  " + piece, end="")
                elif piece == 'K':
                    print("\033[1;33;48m  " + piece, end="")
                elif piece == 'p' or piece == 'r' or piece == 'n' or piece == 'b' or piece == 'q':
                    print("\033[1;31;48m  " + piece, end="")
                elif piece == 'k':
                    print("\033[1;36;48m  " + piece, end="")
            print("\n")

