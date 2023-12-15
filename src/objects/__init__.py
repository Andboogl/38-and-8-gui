"""Game objects (board, player, obstacle, point...)"""


from .board import Board
from .figures import *
from .coordinate_generation import generate_coordinates


__all__ = [
    'Board',
    'figures',
    'generate_coordinates',
    'Player', 'Obstacle', 'Point']
