import random
from coord import Coord


class Field:
    HORIZONTAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MINE = 0
    EMPTY_CELL = 1
    OCCUPIED_CELL = 2

    # width - letters, length - numbers
    def __init__(self, width, length, mines):
        self.width = width
        self.length = length
        self.mines = mines
        self.field_dict = {}
        self.flag_list = []

    def create_field(self):
        for x in range(self.width):
            for y in range(self.length):
                self.field_dict.setdefault(Coord(x, y), ' ')

    def print_field(self, hide_mines=True):
        top_letters = []
        for i in range(self.width):
            top_letters.append(Field.HORIZONTAL[i])
        field_to_print = ''
        field_to_print += ('    ' + '|'.join(top_letters)+'\n')

        for y in range(self.length):
            list_to_print = []
            for x in range(self.width):
                coordinate = Coord(x, y)
                # Doesn't display mines by default.
                if hide_mines:
                    if coordinate in self.flag_list:
                        list_to_print.append('+')
                    elif self.field_dict[coordinate] == '*':
                        list_to_print.append(' ')
                    else:
                        list_to_print.append(self.field_dict[coordinate])
                else:
                    list_to_print.append(self.field_dict[coordinate])
            line = '|'.join(list_to_print)
            if y < 9:
                field_to_print += f'{y+1}--|{line}|\n'
            else:
                field_to_print += f'{y+1}-|{line}|\n'
        return field_to_print

    def set_mines(self):
        for mine in range(self.mines):
            while True:
                rand_cell = random.choice(list(self.field_dict.keys()))
                if self.field_dict[rand_cell] != '*':
                    self.field_dict[rand_cell] = '*'
                    break

    def set_flag(self, flag):
        if self.field_dict[flag] != '*':
            self.field_dict[flag] = '+'
        else:
            self.flag_list.append(flag)

    def annotate(self, y, x):  # minefield = self.field_list #mine_list = self.field_list[y]
        squares = []
        mines = 0
        # Picks nearby squares by increasing and decreasing x indexes by 1
        if self.field_dict[Coord(x, y)] == '*':  # y = y, x = x
            return Field.MINE
        elif self.field_dict[Coord(x, y)] == ' ' or self.field_dict[Coord(x, y)] == '+':
            for y_pointer in range(-1, 2):
                if y + y_pointer > -1:
                    for x_pointer in range(-1, 2):
                        # Avoids adding the x itself
                        if y_pointer == 0 and x_pointer == 0:
                            continue
                        # Avoids wrong indexes by setting the limits
                        elif -1 < x + x_pointer < self.width:
                            # debug line print(y+y_pointer, x+x)
                            try:
                                squares.append(self.field_dict[Coord(x + x_pointer, y + y_pointer)])
                            except KeyError:
                                continue
        else:
            return Field.OCCUPIED_CELL
        # squares = [minefield[y-1][x-1], minefield[y-1][x], minefield[y-1][x+1],
        #            minefield[y][x-1],                             minefield[y][x+1],
        #            minefield[y+1][x-1], minefield[y+1][x], minefield[y+1][x+1]]

        # replaces the square with number and creates a modified line
        for i in squares:
            if i == '*':
                mines += 1

        self.field_dict[Coord(x, y)] = str(mines)
        return Field.EMPTY_CELL


# field = Field(10, 10, 10)
# field.create_field()
# field.set_mines()
# field.print_field(False)
# for x in range(10):
#     for y in range(10):
#         try:
#             field.annotate(x, y)
#             # field.print_field(False)
#         except:
#             pass
# field.print_field(False)
