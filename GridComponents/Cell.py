

class Cell:
    def __init__(self, row=-1, col=-1):
        self.possible_values = list(range(1, 10))
        self.location = (row, col)
        self.row = row
        self.col = col

    def set_value(self, value):
        if self.is_final():
            raise Exception("Cannot set a cell that is already final")
        elif value not in range(1, 10):
            err = "Cannot set cell value to [{}] --- out of valid range".format(value)
            raise Exception(err)
        else:
            self.possible_values = [value]

    def is_final(self):
        return len(self.possible_values) == 1

    def remove_possible_value(self, value):
        if value in self.possible_values and not self.is_final():
            self.possible_values.remove(value)


