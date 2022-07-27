class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(str(self.x)+(str(self.y)))

    def __eq__(self, other):
        return str(self.x)+str(self.y) == str(other.x)+str(other.y)
