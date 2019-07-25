from GridComponents.Cell import Cell
from GridComponents.CellGroup import CellGroup
import math


class CellGroupGrid:
    def __init__(self):
        self.grid_cell_width = 9
        self.grid_cell_height = 9
        self.grid_cells_count = self.grid_cell_width * self.grid_cell_height
        self.grid_group_width = 3
        self.grid_group_height = 3
        self.grid_cell_groups_count = self.grid_group_width * self.grid_group_height
        self.grid_cell_groups = list(map(lambda group_idx: CellGroup(group_idx), range(self.grid_cell_groups_count)))

    def init_grid(self, start_grid):
        # todo: validate start_grid
        for row in range(self.grid_cell_height):
            for col in range(self.grid_cell_width):
                cell = self.get_grid_cell(row, col)
                cell.set_value(start_grid[row][col])

    ####################################################
    # Getters
    ####################################################

    def get_grid_cell(self, row_index, col_index):
        row_groups = list(filter(lambda g: g.group_row == math.floor(row_index / 3), self.grid_cell_groups))
        cell_group = list(filter(lambda g: g.group_col == math.floor(col_index / 3), row_groups))
        if len(cell_group) != 1:
            raise Exception("Cell selection yielded unexpected list of cell groups")
        cells = list(filter(lambda c: c.row == row_index and c.col == col_index, cell_group[0].group_cells))
        if len(cells) != 1:
            raise Exception("Cell selection yielded unexpected list of cells")
        return cells[0]

    def get_grid_cell_row(self, row_index):
        row = []
        for group in list(filter(lambda g: g.group_row == math.floor(row_index / 3), self.grid_cell_groups)):
            cells = list(filter(lambda c: c.row == row_index, group.group_cells))
            row.extend(cells)
        return row

    def get_grid_cell_col(self, col_index):
        col = []
        for group in list(filter(lambda g: g.group_col == col_index % 3, self.grid_cell_groups)):
            cells = list(filter(lambda c: c.col == col_index, group.group_cells))
            col.extend(cells)
        return col

    def get_percent_complete(self):
        final_cells = 0
        for row in range(self.grid_cell_height):
            for col in range(self.grid_cell_width):
                cell = self.get_grid_cell(row, col)
                final_cells += int(cell.is_final())
        return final_cells / self.grid_cells_count

    ####################################################
    # Setters
    ####################################################

    def set_grid_cell_value(self, row_index, col_index, value):
        cell = self.get_grid_cell(row_index, col_index)
        cell.set_value(value)

