class Player1:
    def __init__(self, arr):
        self.arr = arr

    def is_selected_correctly(self, row, col, name):
        if 0 <= row <= 7 and 0 <= col <= 7:  # checking the valid index
            if self.arr[row][col] == name:
                return True
            elif self.arr[row][col] == '0':
                print("Box is empty")
            else:
                print("Wrong piece is selected!")
        else:
            print('Coordinates are invalid!')
        return False

    def is_moveable(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:  # checking the valid index
            if self.arr[row][col] == '0' or self.is_enemy(row, col):
                return True
        return False

    def is_enemy(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:  # checking the valid index
            box = self.arr[row][col]
            if box == 'p' or box == 'r' or box == 'n' or box == 'b' or box == 'k' or box == 'q':
                return True  # if any of the mention player2's pieces found in selected box then return true
        return False

    def is_path_clear(self, start, end, other, name):
        if 0 <= start <= 7 and start <= end <= 7:
            if name == 'row':
                while start + 1 < end:
                    if self.arr[start + 1][other] != '0':
                        return False
                    start += 1
                else:
                    return True
            elif name == 'col':
                while start + 1 < end:
                    if self.arr[other][start + 1] != '0':
                        return False
                    start += 1
                else:
                    return True
            elif name == 'right_to_left':
                while start + 1 < end:
                    if self.arr[start + 1][other - 1] != '0':
                        return False
                    start += 1
                    other -= 1
                else:
                    return True
            elif name == 'left_to_right':
                while start + 1 < end:
                    if self.arr[start + 1][other + 1] != '0':
                        return False
                    start += 1
                    other += 1
                else:
                    return True
        else:
            return False

    def search_for_kill(self, num, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:  # checking the valid index
            if num == 1:
                if self.arr[row][col] == 'R':
                    while row - 1 >= 0:
                        if self.arr[row - 1][col] != '0':
                            if self.is_enemy(row - 1, col):
                                return True
                            else:
                                return False
                        row -= 1
            if num == 3:
                if self.arr[row][col] == 'R':
                    while col + 1 <= 7:
                        if self.arr[row][col + 1] != '0':
                            if self.is_enemy(row, col + 1):
                                return True
                            else:
                                return False
                        col += 1
            if num == 4:
                # checking 1 right diagonal for pawn
                if self.arr[row][col] == 'P':
                    if row + 1 <= 7 and col + 1 <= 7:  # checking index of right diagonal is correct or not
                        if self.arr[row + 1][col + 1] != '0':
                            if self.is_enemy(row + 1, col + 1):
                                return True  # returning true if enemy spotted
            if num == 5:  # checking forward down
                if self.arr[row][col] == 'R':
                    while row + 1 <= 7:
                        if self.arr[row + 1][col] != '0':
                            if self.is_enemy(row + 1, col):
                                return True
                            else:
                                return False
                        row += 1
            if num == 6:
                # checking 1 left diagonal for pawn
                if self.arr[row][col] == 'P':
                    if row + 1 <= 7 and col - 1 >= 0:  # checking index of left diagonal is correct or not
                        if self.arr[row + 1][col - 1] != '0':
                            if self.is_enemy(row + 1, col - 1):
                                return True  # returning true if enemy spotted
            if num == 7:
                if self.arr[row][col] == 'R':
                    while col - 1 >= 0:
                        if self.arr[row][col - 1] != '0':
                            if self.is_enemy(row, col - 1):
                                return True
                            else:
                                return True
                        col -= 1

        return False

    def pawn_mov(self):
        print("Which pawn you want to move?")
        i = int(input("Enter the row num: "))
        j = int(input("Enter the column num: "))
        while not self.is_selected_correctly(i - 1, j - 1, 'P'):  # calling function to check if user selected the
            # correct piece
            print("Please enter the row or column num correctly")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))

        # condition will be true if a pawn can't move forward, left-diagonal and also right-diagonal
        while (self.arr[i][j - 1] != '0') and (not self.search_for_kill(6, i - 1, j - 1)) and (
                not self.search_for_kill(4, i - 1, j - 1)):
            print("This pawn can't move forward")
            print("Again select which Pawn you want to move?")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
            while not self.is_selected_correctly(i - 1, j - 1, 'P'):  # calling function to check if user selected the
                # correct piece
                print("Please enter the row or column num correctly")
                i = int(input("Enter the row num: "))
                j = int(input("Enter the column num: "))
        else:
            # condition will be true if a pawn can't move forward but can move left-diagonal and also right-diagonal
            if (self.arr[i][j - 1] != '0') and (self.search_for_kill(6, i - 1, j - 1)) and (
                    self.search_for_kill(4, i - 1, j - 1)):
                mov = int(input("For left-diagonal enter 6, right-diagonal enter 4 ="))
                while mov != 6 and mov != 4:
                    print("Can't Move")
                    mov = int(input("Please for left-diagonal enter 6, right-diagonal enter 4 ="))
            # condition will be true if a pawn can't move forward and left-diagonal but can move in right-diagonal
            elif self.arr[i][j - 1] != '0' and self.search_for_kill(4, i - 1, j - 1):
                mov = 4
            # condition will be true if a pawn can't move forward and right-diagonal but can move in left-diagonal
            elif self.arr[i][j - 1] != '0' and self.search_for_kill(6, i - 1, j - 1):
                mov = 6
            else:
                left_enemy = True
                right_enemy = True
                if i - 1 == 1:  # checking if the pawing moving 1st time or not
                    mov = int(
                        input("For 1 step enter 1, 2 steps enter 2, left-diagonal enter 6, right-diagonal enter 4 = "))
                    while mov != 1 and mov != 2 and mov != 6 and mov != 4:  # checking for correct input
                        print("Can't move!")
                        mov = int(
                            input(
                                "For 1 step enter 1, 2 steps enter 2, left-diagonal enter 6, right-diagonal enter 4 = "))
                    else:
                        # condition will be true if a pawn have to move forward 2 steps
                        # but the path is not empty
                        while mov == 2 and (self.arr[i + 1][j - 1] != '0' or self.arr[i][j - 1] != '0'):
                            print("Can't move!")
                            # since pawn can't move 2 steps then we are asking for another valid input for movement
                            mov = int(input("For 1 step enter 1, left-diagonal enter 6, right-diagonal enter 4 = "))
                            while mov != 1 and mov != 6 and mov != 4:
                                print("Can't move!")
                                mov = int(input("For 1 step enter 1, left-diagonal enter 6, right-diagonal enter 4 = "))

                        # condition will be true if a pawn have to move left-diagonal but it can't cuz there is not enemy
                        # it will also be true if pawn have to move right-diagonal but it can't for same reason
                        while (mov == 6 and not self.search_for_kill(mov, i - 1, j - 1)) or (
                                mov == 4 and not self.search_for_kill(mov, i - 1, j - 1)):

                            # checking if pawn can't move to left-diagonal then we are asking for valid input
                            if mov == 6:
                                print("Can't move!")
                                left_enemy = False

                                # This condition helps to control the execution of this code more than 1 time
                                if right_enemy:
                                    mov = int(input("For 1 step enter 1, 2 steps enter 2, right-diagonal enter 4 = "))
                                    while mov != 1 and mov != 2 and mov != 4:
                                        print("Can't move!")
                                        mov = int(
                                            input("For 1 step enter 1, 2 steps enter 2, right-diagonal enter 4 = "))

                            # checking if pawn can't move to left-diagonal then we are asking for valid input
                            elif mov == 4:
                                print("Can't move!")
                                right_enemy = False

                                # This condition helps to control the execution of this code more than 1 time
                                if left_enemy:
                                    mov = int(input("For 1 step enter 1, 2 steps enter 2, left-diagonal enter 6 = "))
                                    while mov != 1 and mov != 2 and mov != 6:
                                        print("Can't move!")
                                        mov = int(
                                            input("For 1 step enter 1, 2 steps enter 2, left-diagonal enter 6 = "))

                            # This condition will be true if a pawn tries to go in both diagonal steps but can't
                            # and then it will force the pawn to move only forward
                            if not left_enemy and not right_enemy:
                                mov = int(input("For 1 step enter 1, 2 steps enter 2 = "))
                                while mov != 1 and mov != 2:
                                    print("Can't move!")
                                    mov = int(input("For 1 step enter 1, 2 steps enter 2 = "))
                else:  # else will be executed if pawn is not moving 1st time
                    mov = int(input("For 1 step enter 1, left-diagonal enter 6, right-diagonal enter 4 = "))
                    while mov != 1 and mov != 6 and mov != 4:
                        print("Can't move!")
                        mov = int(input("For 1 step enter 1, left-diagonal enter 6, right-diagonal enter 4 = "))
                    else:  # else will run only if we get valid mov value

                        # condition will be true if a pawn have to move left-diagonal but it can't cuz there is not enemy
                        # it will also be true if pawn have to move right-diagonal but it can't for same reason
                        while (mov == 6 and not self.search_for_kill(mov, i - 1, j - 1)) or (
                                mov == 4 and not self.search_for_kill(mov, i - 1, j - 1)):

                            # checking if pawn can't move to left-diagonal then we are asking for valid input
                            if mov == 6:
                                print("Can't move!")
                                left_enemy = False

                                # This condition helps to control the execution of this code more than 1 time
                                if right_enemy:
                                    mov = int(input("For 1 step enter 1, right-diagonal enter 4 = "))
                                    while mov != 1 and mov != 4:
                                        print("Can't move!")
                                        mov = int(input("For 1 step enter 1, right-diagonal enter 4 = "))

                            # checking if pawn can't move to left-diagonal then we are asking for valid input
                            elif mov == 4:
                                print("Can't move!")
                                right_enemy = False

                                # This condition helps to control the execution of this code more than 1 time
                                if left_enemy:
                                    mov = int(input("For 1 step enter 1, left-diagonal enter 6 = "))
                                    while mov != 1 and mov != 6:
                                        print("Can't move!")
                                        mov = int(input("For 1 step enter 1, left-diagonal enter 6 = "))

                            # This condition will be true if a pawn tries to go in both diagonal steps but can't
                            # and then it will force the pawn to move only forward
                            if not left_enemy and not right_enemy:
                                mov = 1
                                print("You can only move forward!")
            if mov == 1:  # moving the pawn 1 step forward and checking forward 1
                # box is empty or not
                self.arr[i][j - 1] = self.arr[i - 1][j - 1]
                self.arr[i - 1][j - 1] = '0'
                if i == 7:  # if pawn reaches to the end of opponent's 1st row then it will changes to Queen
                    self.arr[i][j - 1] = 'Q'
            elif mov == 2:  # moving the pawn 2
                # steps forward and checking forward 2 boxes are empty or not
                self.arr[i + 1][j - 1] = self.arr[i - 1][j - 1]
                self.arr[i - 1][j - 1] = '0'
            elif mov == 6:
                self.arr[i][j - 2] = self.arr[i - 1][j - 1]
                self.arr[i - 1][j - 1] = '0'
                if i == 7:  # if pawn reaches to the end of opponent's 1st row then it will changes to Queen
                    self.arr[i][j - 2] = 'Q'
            elif mov == 4:
                self.arr[i][j] = self.arr[i - 1][j - 1]
                self.arr[i - 1][j - 1] = '0'
                if i == 7:  # if pawn reaches to the end of opponent's 1st row then it will changes to Queen
                    self.arr[i][j] = 'Q'
            else:
                print("Can't move!")

    def rook_move(self):
        print("Which rook you want to move?")
        i = int(input("Enter the row num: "))
        j = int(input("Enter the column num: "))
        while not self.is_selected_correctly(i - 1, j - 1, 'R'):  # calling function to check if user selected the
            # correct piece
            print("Please enter the row or column num correctly")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
        while (not self.is_moveable(i - 2, j - 1)) and (not self.is_moveable(i, j - 1)) and (
                not self.is_moveable(i - 1, j - 2)) and (not self.is_moveable(i - 1, j)):
            print("This rook can't move")
            print("Which rook you want to move?")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
            while not self.is_selected_correctly(i - 1, j - 1, 'R'):  # calling function to check if user selected the
                # correct piece
                print("Please enter the row or column num correctly")
                i = int(input("Enter the row num: "))
                j = int(input("Enter the column num: "))

        else:
            dic = input("Please enter the direction(L,R,U,D): ").lower()
            while dic != 'l' and dic != 'r' and dic != 'u' and dic != 'd':
                dic = input("Please enter the direction correctly(L,R,U,D): ").lower()
            while (dic == 'l' and not self.is_moveable(i - 1, j - 2)) or (
                    dic == 'r' and not self.is_moveable(i - 1, j)) or (
                    dic == 'u' and not self.is_moveable(i - 2, j - 1)) or (
                    dic == 'd' and not self.is_moveable(i, j - 1)):
                print("Can't move in that direction")
                dic = input("Please enter the direction correctly(L,R,U,D): ").lower()
                while dic != 'l' and dic != 'r' and dic != 'u' and dic != 'd':
                    dic = input("Please enter the direction correctly(L,R,U,D): ").lower()
            else:
                mov = int(input("Please enter the number of steps you want to move = "))
                while mov <= 0:
                    print("Invalid move!")
                    mov = int(input("Please enter the number of steps you want to move = "))
                else:
                    if dic == 'd':
                        while (i - 1 + mov > 7) or (not self.is_path_clear(i - 1, i - 1 + mov, j - 1, 'row')) or (
                                self.arr[i - 1 + mov][j - 1] != '0' and not self.is_enemy(i - 1 + mov, j - 1)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 + mov][j - 1] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == 'r':
                        while (j - 1 + mov > 7) or (not self.is_path_clear(j - 1, j - 1 + mov, i - 1, 'col') or (
                                self.arr[i - 1][j - 1 + mov] != '0' and not self.is_enemy(i - 1, j - 1 + mov))):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1][j - 1 + mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == 'u':
                        while (i - 1 - mov < 0) or (not self.is_path_clear(i - 1 - mov, i - 1, j - 1, 'row')) or (
                                self.arr[i - 1 - mov][j - 1] != '0' and not self.is_enemy(i - 1 - mov, j - 1)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 - mov][j - 1] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == 'l':
                        while (j - 1 - mov < 0) or (not self.is_path_clear(j - 1 - mov, j - 1, i - 1, 'col')) or (
                                self.arr[i - 1][j - 1 - mov] != '0' and not self.is_enemy(i - 1, j - 1 - mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1][j - 1 - mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'

    def bishop_move(self):
        print("Which bishop you want to move?")
        i = int(input("Enter the row num: "))
        j = int(input("Enter the column num: "))
        while not self.is_selected_correctly(i - 1, j - 1, 'B'):  # calling function to check if user selected the
            # correct piece
            print("Please enter the row or column num correctly")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
        while (not self.is_moveable(i - 2, j - 2)) and (not self.is_moveable(i, j)) and (
                not self.is_moveable(i - 2, j)) and (not self.is_moveable(i, j - 2)):
            print("This bishop can't move")
            print("Which bishop you want to move?")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
            while not self.is_selected_correctly(i - 1, j - 1, 'B'):  # calling function to check if user selected the
                # correct piece
                print("Please enter the row or column num correctly")
                i = int(input("Enter the row num: "))
                j = int(input("Enter the column num: "))
        else:
            dic = input(
                "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                "Please enter the direction(2,4,6,8): ")
            while dic != '2' and dic != '4' and dic != '6' and dic != '8':
                dic = input(
                    "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                    "Please enter the direction(2,4,6,8): ")
            while (dic == '2' and not self.is_moveable(i - 2, j)) or (
                    dic == '4' and not self.is_moveable(i, j)) or (
                    dic == '6' and not self.is_moveable(i, j - 2)) or (
                    dic == '8' and not self.is_moveable(i - 2, j - 2)):
                print("Can't move in that direction")
                dic = input(
                    "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                    "Please enter the direction(2,4,6,8): ")
                while dic != '2' and dic != '4' and dic != '6' and dic != '8':
                    dic = input(
                        "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                        "Please enter the direction(2,4,6,8): ")
            else:
                mov = int(input("Please enter the number of steps you want to move = "))
                while mov <= 0:
                    print("Invalid move!")
                    mov = int(input("Please enter the number of steps you want to move = "))
                else:
                    if dic == '6':
                        while (i - 1 + mov > 7 or j - 1 - mov < 0) or (
                                not self.is_path_clear(i - 1, i - 1 + mov, j - 1, 'right_to_left')) or (
                                self.arr[i - 1 + mov][j - 1 - mov] != '0' and not self.is_enemy(i - 1 + mov,
                                                                                                j - 1 - mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 + mov][j - 1 - mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == '4':
                        while (i - 1 + mov > 7 or j - 1 + mov > 7) or (
                                not self.is_path_clear(i - 1, i - 1 + mov, j - 1, 'left_to_right')) or (
                                self.arr[i - 1 + mov][j - 1 + mov] != '0' and not self.is_enemy(i - 1 + mov,
                                                                                                j - 1 + mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 + mov][j - 1 + mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == '2':
                        while (i - 1 - mov < 0 or j - 1 + mov > 7) or (
                                not self.is_path_clear(i - 1 - mov, i - 1, j - 1 + mov, 'right_to_left')) or (
                                self.arr[i - 1 - mov][j - 1 + mov] != '0' and not self.is_enemy(i - 1 - mov,
                                                                                                j - 1 + mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 - mov][j - 1 + mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == '8':
                        while (j - 1 - mov < 0 or i - 1 - mov < 0) or (
                                not self.is_path_clear(i - 1 - mov, i - 1, j - 1 - mov, 'left_to_right') or (
                                self.arr[i - 1 - mov][j - 1 - mov] != '0' and not self.is_enemy(i - 1 - mov,
                                                                                                j - 1 - mov))):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 - mov][j - 1 - mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'

    def queen_move(self):
        print("Enter the coordinates of a queen!")
        i = int(input("Enter the row num: "))
        j = int(input("Enter the column num: "))
        while not self.is_selected_correctly(i - 1, j - 1, 'Q'):  # calling function to check if user selected the
            # correct piece
            print("Please enter the row or column num correctly")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
        while (not self.is_moveable(i - 2, j - 1)) and (not self.is_moveable(i, j - 1)) and (
                not self.is_moveable(i - 1, j - 2)) and (not self.is_moveable(i - 1, j)) and (
                not self.is_moveable(i - 2, j - 2)) and (not self.is_moveable(i, j)) and (
                not self.is_moveable(i - 2, j)) and (not self.is_moveable(i, j - 2)):
            print("Queen can't move")
            return False
        else:
            dic = input(
                "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
            while dic != 'l' and dic != 'r' and dic != 'u' and dic != 'd' and dic != '2' and dic != '4' and dic != '6' and dic != '8':
                dic = input(
                    "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                    "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
            while (dic == 'l' and not self.is_moveable(i - 1, j - 2)) or (
                    dic == 'r' and not self.is_moveable(i - 1, j)) or (
                    dic == 'u' and not self.is_moveable(i - 2, j - 1)) or (
                    dic == 'd' and not self.is_moveable(i, j - 1)) or (
                    dic == '2' and not self.is_moveable(i - 2, j)) or (
                    dic == '4' and not self.is_moveable(i, j)) or (
                    dic == '6' and not self.is_moveable(i, j - 2)) or (
                    dic == '8' and not self.is_moveable(i - 2, j - 2)):
                print("Can't move in that direction")
                dic = input(
                    "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                    "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
                while dic != 'l' and dic != 'r' and dic != 'u' and dic != 'd' and dic != '2' and dic != '4' and dic != '6' and dic != '8':
                    dic = input(
                        "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                        "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
            else:
                mov = int(input("Please enter the number of steps you want to move = "))
                while mov <= 0:
                    print("Invalid move!")
                    mov = int(input("Please enter the number of steps you want to move = "))
                else:
                    if dic == 'd':
                        while (i - 1 + mov > 7) or (not self.is_path_clear(i - 1, i - 1 + mov, j - 1, 'row')) or (
                                self.arr[i - 1 + mov][j - 1] != '0' and not self.is_enemy(i - 1 + mov, j - 1)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 + mov][j - 1] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == 'r':
                        while (j - 1 + mov > 7) or (not self.is_path_clear(j - 1, j - 1 + mov, i - 1, 'col') or (
                                self.arr[i - 1][j - 1 + mov] != '0' and not self.is_enemy(i - 1, j - 1 + mov))):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1][j - 1 + mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == 'u':
                        while (i - 1 - mov < 0) or (not self.is_path_clear(i - 1 - mov, i - 1, j - 1, 'row')) or (
                                self.arr[i - 1 - mov][j - 1] != '0' and not self.is_enemy(i - 1 - mov, j - 1)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 - mov][j - 1] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == 'l':
                        while (j - 1 - mov < 0) or (not self.is_path_clear(j - 1 - mov, j - 1, i - 1, 'col')) or (
                                self.arr[i - 1][j - 1 - mov] != '0' and not self.is_enemy(i - 1, j - 1 - mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1][j - 1 - mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == '6':
                        while (i - 1 + mov > 7 or j - 1 - mov < 0) or (
                                not self.is_path_clear(i - 1, i - 1 + mov, j - 1, 'right_to_left')) or (
                                self.arr[i - 1 + mov][j - 1 - mov] != '0' and not self.is_enemy(i - 1 + mov,
                                                                                                j - 1 - mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 + mov][j - 1 - mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == '4':
                        while (i - 1 + mov > 7 or j - 1 + mov > 7) or (
                                not self.is_path_clear(i - 1, i - 1 + mov, j - 1, 'left_to_right')) or (
                                self.arr[i - 1 + mov][j - 1 + mov] != '0' and not self.is_enemy(i - 1 + mov,
                                                                                                j - 1 + mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 + mov][j - 1 + mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == '2':
                        while (i - 1 - mov < 0 or j - 1 + mov > 7) or (
                                not self.is_path_clear(i - 1 - mov, i - 1, j - 1 + mov, 'right_to_left')) or (
                                self.arr[i - 1 - mov][j - 1 + mov] != '0' and not self.is_enemy(i - 1 - mov,
                                                                                                j - 1 + mov)):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 - mov][j - 1 + mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'
                    elif dic == '8':
                        while (j - 1 - mov < 0 or i - 1 - mov < 0) or (
                                not self.is_path_clear(i - 1 - mov, i - 1, j - 1 - mov, 'left_to_right') or (
                                self.arr[i - 1 - mov][j - 1 - mov] != '0' and not self.is_enemy(i - 1 - mov,
                                                                                                j - 1 - mov))):
                            print("Can't move!")
                            mov = int(input("Please enter the number of steps you want to move = "))
                            while mov <= 0:
                                print("Invalid move!")
                                mov = int(input("Please enter the number of steps you want to move = "))
                        else:
                            self.arr[i - 1 - mov][j - 1 - mov] = self.arr[i - 1][j - 1]
                            self.arr[i - 1][j - 1] = '0'

    def king_mov(self):
        print("Enter the coordinates of a king!")
        i = int(input("Enter the row num: "))
        j = int(input("Enter the column num: "))
        while not self.is_selected_correctly(i - 1, j - 1, 'K'):  # calling function to check if user selected the
            # correct piece
            print("Please enter the row or column num correctly")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
        while (not self.is_moveable(i - 2, j - 1)) and (not self.is_moveable(i, j - 1)) and (
                not self.is_moveable(i - 1, j - 2)) and (not self.is_moveable(i - 1, j)) and (
                not self.is_moveable(i - 2, j - 2)) and (not self.is_moveable(i, j)) and (
                not self.is_moveable(i - 2, j)) and (not self.is_moveable(i, j - 2)):
            print("King can't move")
            return False
        else:
            dic = input(
                "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
            while dic != 'l' and dic != 'r' and dic != 'u' and dic != 'd' and dic != '2' and dic != '4' and dic != '6' and dic != '8':
                dic = input(
                    "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                    "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
            while (dic == 'l' and not self.is_moveable(i - 1, j - 2)) or (
                    dic == 'r' and not self.is_moveable(i - 1, j)) or (
                    dic == 'u' and not self.is_moveable(i - 2, j - 1)) or (
                    dic == 'd' and not self.is_moveable(i, j - 1)) or (
                    dic == '2' and not self.is_moveable(i - 2, j)) or (
                    dic == '4' and not self.is_moveable(i, j)) or (
                    dic == '6' and not self.is_moveable(i, j - 2)) or (
                    dic == '8' and not self.is_moveable(i - 2, j - 2)):
                print("Can't move in that direction")
                dic = input(
                    "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                    "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
                while dic != 'l' and dic != 'r' and dic != 'u' and dic != 'd' and dic != '2' and dic != '4' and dic != '6' and dic != '8':
                    dic = input(
                        "2 = Upper Right Diagonal, 4 = Lower Right Diagonal, 6 = Lower Left Diagonal, 8 = Upper Left Diagonal\n"
                        "Please enter the direction(2,4,6,8,L,R,U,D): ").lower()
            else:
                mov = 1
                if dic == 'd':
                    self.arr[i - 1 + mov][j - 1] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'r':
                    self.arr[i - 1][j - 1 + mov] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'u':
                    self.arr[i - 1 - mov][j - 1] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'l':
                    self.arr[i - 1][j - 1 - mov] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == '6':
                    self.arr[i - 1 + mov][j - 1 - mov] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == '4':
                    self.arr[i - 1 + mov][j - 1 + mov] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == '2':
                    self.arr[i - 1 - mov][j - 1 + mov] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == '8':
                    self.arr[i - 1 - mov][j - 1 - mov] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'

    def knight_move(self):
        print("Which knight you want to move?")
        i = int(input("Enter the row num: "))
        j = int(input("Enter the column num: "))
        while not self.is_selected_correctly(i - 1, j - 1, 'N'):  # calling function to check if user selected the
            # correct piece
            print("Please enter the row or column num correctly")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
        while (not self.is_moveable(i - 3, j - 2)) and (not self.is_moveable(i - 3, j)) and (
                not self.is_moveable(i + 1, j - 2)) and (not self.is_moveable(i + 1, j)) and (
                not self.is_moveable(i - 2, j - 3)) and (not self.is_moveable(i, j - 3)) and (
                not self.is_moveable(i - 2, j + 1)) and (not self.is_moveable(i, j + 1)):
            print("This knight can't move")
            print("Which knight you want to move?")
            i = int(input("Enter the row num: "))
            j = int(input("Enter the column num: "))
            while not self.is_selected_correctly(i - 1, j - 1, 'N'):  # calling function to check if user selected the
                # correct piece
                print("Please enter the row or column num correctly")
                i = int(input("Enter the row num: "))
                j = int(input("Enter the column num: "))
        else:
            dic = input("D = Down, U = Up, L = Left, R = Right\n"
                        "Please enter the direction(DL,DR,UL,UR,LU,LD,RU,RD): ").lower()
            while dic != 'dl' and dic != 'dr' and dic != 'ul' and dic != 'ur' and dic != 'lu' and dic != 'ld' and dic != 'ru' and dic != 'rd':
                dic = input("D = Down, U = Up, L = Left, R = Right\n"
                            "Please enter the direction(DL,DR,UL,UR,LU,LD,RU,RD): ").lower()
            while (dic == 'dl' and not self.is_moveable(i + 1, j - 2)) or (
                    dic == 'dr' and not self.is_moveable(i + 1, j)) or (
                    dic == 'ul' and not self.is_moveable(i - 3, j - 2)) or (
                    dic == 'ur' and not self.is_moveable(i - 3, j)) or (
                    dic == 'lu' and not self.is_moveable(i - 2, j - 3)) or (
                    dic == 'ld' and not self.is_moveable(i, j - 3)) or (
                    dic == 'ru' and not self.is_moveable(i - 2, j + 1)) or (
                    dic == 'rd' and not self.is_moveable(i, j + 1)):
                print("Can't move in that direction")
                dic = input("D = Down, U = Up, L = Left, R = Right\n"
                            "Please enter the direction(DL,DR,UL,UR,LU,LD,RU,RD): ").lower()
                while dic != 'dl' and dic != 'dr' and dic != 'ul' and dic != 'ur' and dic != 'lu' and dic != 'ld' and dic != 'ru' and dic != 'rd':
                    dic = input("D = Down, U = Up, L = Left, R = Right\n"
                                "Please enter the direction(DL,DR,UL,UR,LU,LD,RU,RD): ").lower()
            else:
                if dic == 'dl':
                    self.arr[i + 1][j - 2] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'dr':
                    self.arr[i + 1][j] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'ul':
                    self.arr[i - 3][j - 2] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'ur':
                    self.arr[i - 3][j] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'lu':
                    self.arr[i - 2][j - 3] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'ld':
                    self.arr[i][j - 3] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'ru':
                    self.arr[i - 2][j + 1] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
                elif dic == 'rd':
                    self.arr[i][j + 1] = self.arr[i - 1][j - 1]
                    self.arr[i - 1][j - 1] = '0'
