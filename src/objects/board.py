"""Board"""


from .figures import Empty
from .figures import Point
from .figures import Obstacle


class Board:
    """Board"""
    def __init__(self, width, height):
        self.__board_mas = [
            [Empty() for _ in range(width)]
            for _ in range(height)
        ]

        # For player correct moves
        self.width = width
        self.height = height

    def put_figures(self, *args):
        """Put a lot of figures to the board"""
        for figure in args:
            self.put_figure(figure)

    def is_win(self):
        """Return True if there is no points on board. Else False"""
        for row in self.__board_mas:
            for item in row:
                if isinstance(item, Point):
                    return False

        return True

    def count_of_points(self):
        """Staple the number of points to the board"""
        points = 0

        for row in self.__board_mas:
            for field in row:
                if isinstance(field, Point):
                    points += 1

        return points

    def move_player(self, player_obj, where):
        """Move player"""
        if where in player_obj.get_moves(self):
            if isinstance(self.__board_mas[where[0]][where[1]], Point):
                player_obj.add_collected_point()

            if isinstance(self.__board_mas[where[0]][where[1]], Obstacle):
                player_obj.add_broken_obstacle()

            self.__board_mas[where[0]][where[1]] = player_obj
            self.__board_mas[player_obj.x][player_obj.y] = Empty()
            player_obj.x, player_obj.y = where
            player_obj.add_move()

        else:
            raise ValueError('Player can\'t do this move')

    def put_figure(self, figure_obj):
        """Put figure"""
        x = figure_obj.x
        y = figure_obj.y

        if isinstance(self.__board_mas[x][y], Empty):
            self.__board_mas[figure_obj.x][figure_obj.y] = figure_obj

        else:
            raise ValueError(f'self.__board_mas[{x}][{y}] != Empty')

    @property
    def board_mas(self):
        """Get board mas (for player moves)"""
        return self.__board_mas

    def __str__(self):
        """str(Board())"""
        res = ''
        for row in self.__board_mas:
            res += '  '.join(map(str, row)) + '\n'

        return res
