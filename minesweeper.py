from field2 import Field
from coord import Coord


def check_number(number, limit):
    if number.isdecimal():
        number = int(number)
        if 0 < number <= limit:
            return True


def check_move(move):
    move_coord = []
    try:
        square = Field.HORIZONTAL.index(move[0].upper())
        move_coord.append(square)
    except:
        pass

    try:
        row = int(move[1:]) - 1
        move_coord.append(row)
    except:
        pass
    return move_coord


class Minesweeper:

    def __init__(self):
        self.field = None

    def initiate_game(self):
        while True:
            print('Please, select a width of the field. (from 1 to 26)')
            width = input()
            if check_number(width, 26):
                width = int(width)
                break

        while True:
            print('Please, select a length of the field. (from 1 to 99)')
            length = input()
            if check_number(length, 99):
                length = int(length)
                break

        mines_limit = width * length

        while True:
            print('Please, select a valid number of mines.')
            print('(no more than a number of cells)')
            mines = input()
            if check_number(mines, mines_limit):
                mines = int(mines)
                break

        self.field = Field(width, length, mines)
        self.field.create_field()
        self.field.set_mines()

    def player_move(self):

        while True:
            print(self.field.print_field())
            print('Pick a valid square. Type letter and number(a1, b2, c3, etc.)')
            move = input()

            if move.startswith('+'):
                move = move[1:]
                move_coord = check_move(move)
                try:
                    flag = Coord(move_coord[0], move_coord[1])
                    print(move_coord[0], move_coord[1])
                    if flag not in self.field.flag_list:
                        self.field.set_flag(flag)
                    else:
                        continue
                except:
                    continue
            else:
                move_coord = check_move(move)
                try:
                    return self.field.annotate(move_coord[1], move_coord[0])
                except:
                    continue

    def check_player_won(self):
        for square in self.field.field_dict:
            if self.field.field_dict[square] == ' ':
                return False
        return True
