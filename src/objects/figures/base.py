"""Base for all figures"""


class Empty:
    """Empty field"""
    def __str__(self):
        """str(Empty())"""
        return '·'


class Figure:
    """Base class for all figures"""
    x: int
    y: int
    img: str

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """str(Figure())"""
        return self.img
