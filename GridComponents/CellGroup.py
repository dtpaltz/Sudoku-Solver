from GridComponents.Cell import Cell
import math


class CellGroup:
    def __init__(self, group_index):
        self.group_index = group_index
        self.group_row = math.floor(group_index / 3)
        self.group_col = math.floor(group_index % 3)
        self.group_cells = []
        self.init_group_cells()

    def init_group_cells(self):
        if len(self.group_cells) == 0:
            for row in range(int(self.group_row * 3), int(self.group_row * 3) + 3):
                for col in range(int(self.group_col * 3), int(self.group_col * 3) + 3):
                    self.group_cells.append(Cell(row, col))


