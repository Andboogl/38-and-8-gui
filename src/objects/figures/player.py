"""Player"""


from .base import Figure, Empty
from .point import Point
from .obstacle import Obstacle


class Player(Figure):
    """Player"""
    img = '•'
    __points_collected = 0
    __obstacles_broken = 0
    __moves_count = 0

    @property
    def moves_count(self):
        return self.__moves_count

    @property
    def obstacles_broken(self):
        return self.__obstacles_broken

    @property
    def points_collected(self):
        return self.__points_collected

    def add_collected_point(self):
        self.__points_collected += 1

    def add_broken_obstacle(self):
        self.__obstacles_broken += 1

    def add_move(self):
        self.__moves_count += 1

    def get_moves(self, board):
        """Get player moves"""
        board_mas = board.board_mas
        moves = []  # Moves

        if self.x < board.height - 1:
            if isinstance(board_mas[self.x + 1][self.y], Empty) or isinstance(board_mas[self.x + 1][self.y], Point):
                moves.append([self.x + 1, self.y])
        
            elif isinstance(board_mas[self.x + 1][self.y], Obstacle):
                if self.__obstacles_broken < 3:
                    moves.append([self.x + 1, self.y])

        if self.x > 0:
            if isinstance(board_mas[self.x - 1][self.y], Empty) or isinstance(board_mas[self.x - 1][self.y], Point):
                moves.append([self.x - 1, self.y])

            elif isinstance(board_mas[self.x - 1][self.y], Obstacle):
                if self.__obstacles_broken < 3:
                    moves.append([self.x - 1, self.y])

        if self.y < board.width - 1:
            if isinstance(board_mas[self.x][self.y + 1], Empty) or isinstance(board_mas[self.x][self.y + 1], Point):
                moves.append([self.x, self.y + 1])

            elif isinstance(board_mas[self.x][self.y + 1], Obstacle):
                if self.__obstacles_broken < 3:
                    moves.append([self.x, self.y + 1])

        if self.y > 0:
            if isinstance(board_mas[self.x][self.y - 1], Empty) or isinstance(board_mas[self.x][self.y - 1], Point):
                moves.append([self.x, self.y - 1])

            elif isinstance(board_mas[self.x][self.y - 1], Obstacle):
                if self.__obstacles_broken < 3:
                    moves.append([self.x, self.y - 1])

        return moves
