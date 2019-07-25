import enum

class StartingGridConfigurations(enum.Enum):

    level_0 = [
        [3, 7, 4, 1, 2, 6, 9, 8, 5],
        [1, 5, 8, 4, 9, 7, 6, 3, 2],
        [6, 9, 2, 8, 5, 3, 1, 7, 4],
        [2, 8, 6, 5, 7, 1, 4, 9, 3],
        [7, 4, 3, 9, 6, 2, 8, 5, 1],
        [9, 1, 5, 3, 8, 4, 2, 6, 7],
        [8, 6, 7, 2, 1, 5, 3, 4, 9],
        [4, 2, 9, 7, 3, 8, 5, 1, 6],
        [5, 3, 1, 6, 4, 9, 7, 2, 8]
    ]

    level_1 = [
        [3, 7, 4, 1, 0, 6, 9, 8, 5],
        [1, 5, 8, 4, 0, 7, 6, 3, 2],
        [6, 9, 2, 8, 5, 3, 1, 7, 4],
        [2, 0, 0, 5, 7, 1, 0, 0, 3],
        [7, 4, 0, 9, 0, 2, 0, 5, 1],
        [0, 1, 5, 0, 0, 0, 2, 6, 0],
        [8, 6, 7, 2, 1, 5, 3, 4, 9],
        [4, 2, 9, 7, 3, 8, 5, 1, 6],
        [5, 0, 1, 6, 0, 9, 7, 0, 8]
    ]

    level_2 = [
        [0, 3, 8, 1, 0, 2, 5, 6, 0],
        [5, 0, 1, 0, 6, 0, 4, 0, 2],
        [6, 2, 0, 9, 0, 4, 0, 1, 3],
        [2, 0, 9, 0, 0, 0, 1, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 3, 0],
        [7, 0, 3, 0, 0, 0, 2, 0, 5],
        [9, 6, 0, 7, 0, 8, 0, 5, 1],
        [3, 0, 5, 0, 2, 0, 7, 0, 4],
        [0, 7, 4, 5, 0, 9, 6, 2, 0]
    ]

    level_3 = [
        [0, 3, 9, 0, 0, 0, 8, 1, 0],
        [8, 0, 0, 1, 0, 9, 0, 0, 2],
        [7, 0, 0, 0, 6, 0, 0, 0, 3],
        [0, 6, 0, 5, 0, 7, 0, 4, 0],
        [0, 0, 7, 0, 9, 0, 6, 0, 0],
        [0, 2, 0, 4, 0, 6, 0, 3, 0],
        [6, 0, 0, 0, 2, 0, 0, 0, 4],
        [4, 0, 0, 3, 0, 8, 0, 0, 7],
        [0, 8, 1, 0, 0, 0, 9, 2, 0]
    ]