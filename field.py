import random


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
        self.field_list = []
        self.flag_list = []

    def create_field(self):
        for i in range(self.length):
            line = []            
            for x in range(self.width):
                line.append(' ')           
            self.field_list.append(line)        

    def print_field(self, hide_mines=True):
        top_letters = []
        for i in range(self.width):
            top_letters.append(Field.HORIZONTAL[i])    
        print('    ' + '|'.join(top_letters))
        for index, row in enumerate(self.field_list, start=1):
            list_to_print = []
            for i in row:
                # Doesn't display mines by default.
                if hide_mines:
                    if i == '*':
                        list_to_print.append(' ')
                    else:
                        list_to_print.append(i)
                else:
                    list_to_print.append(i)                    
            line = '|'.join(list_to_print)
            if index < 10:
                print(f'{index}--|{line}|')
            else:
                print(f'{index}-|{line}|')
        print()

    def set_mines(self):
        for mine in range(self.mines):
            while True:
                rand_length = random.randrange(self.length)
                rand_width = random.randrange(self.width)
                if self.field_list[rand_length][rand_width] != '*':
                    self.field_list[rand_length][rand_width] = '*'
                    break

    def annotate(self, row, square):  # minefield = self.field_list #mine_list = self.field_list[row]
        squares = []
        mines = 0
        # Picks nearby squares by increasing and decreasing square indexes by 1
        if self.field_list[row][square] == '*':  # row = number, square = letter
            return Field.MINE
        elif self.field_list[row][square] == ' ':
            for i in range(-1, 2):
                if row+i > -1:                              
                    for x in range(-1, 2):
                        # Avoids adding the square itself
                        if i == 0 and x == 0:
                            continue
                        # Avoids wrong indexes by setting the limits
                        elif -1 < square+x < self.width:
                            # debug line print(row+i, square+x)
                            try:
                                squares.append(self.field_list[row+i][square+x])              
                            except IndexError:
                                continue
        else:
            return Field.OCCUPIED_CELL
        # squares = [minefield[row-1][square-1], minefield[row-1][square], minefield[row-1][square+1],
        #            minefield[row][square-1],                             minefield[row][square+1],
        #            minefield[row+1][square-1], minefield[row+1][square], minefield[row+1][square+1]]

    # replaces the square with number and creates a modified line
        for i in squares:
            if i == '*':
                mines += 1

        self.field_list[row][square] = str(mines)    
        return Field.EMPTY_CELL
