"""Coordinate generation"""


import random


def generate(board_width, board_height, count=25, numbers_list=[], /):
    """Generate unique coordinates of shapes"""

    if 0 < count:
        number = random.randint(0, board_width-1)
        number2 = random.randint(0, board_height-1)

        if [number, number2] in numbers_list:
            generate(board_width, board_height, count - 1, numbers_list)

        else:
            numbers_list.append([number, number2])

        generate(board_width, board_height, count - 1, numbers_list)

    return numbers_list
