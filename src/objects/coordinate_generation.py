"""Coordinate generation"""


import random


def generate_coordinates(board_width, board_height, count):
    """Generate unique coordinates of shapes"""

    numbers = []

    while len(numbers) <= count:
        coor = [random.randint(0, board_width), random.randint(0, board_height)]

        while coor in numbers:
            coor = [random.randint(0, board_width), random.randint(0, board_height)]

        numbers.append(coor)

    return numbers
