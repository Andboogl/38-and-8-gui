"""Player"""


from .base import Figure, Empty
from .point import Point


class Player(Figure):
    """Player"""
    img = '•'

    def get_moves(self, board):
        """Get player moves"""
        board_mas = board.board_mas
        moves = []  # Moves

        if self.x < board.height - 1:
            if isinstance(board_mas[self.x + 1][self.y], Empty) or isinstance(board_mas[self.x + 1][self.y], Point):
                moves.append([self.x + 1, self.y])

        if self.x > 0:
            if isinstance(board_mas[self.x - 1][self.y], Empty) or isinstance(board_mas[self.x - 1][self.y], Point):
                moves.append([self.x - 1, self.y])

        if self.y < board.width - 1:
            if isinstance(board_mas[self.x][self.y + 1], Empty) or isinstance(board_mas[self.x][self.y + 1], Point):
                moves.append([self.x, self.y + 1])

        if self.y > 0:
            if isinstance(board_mas[self.x][self.y - 1], Empty) or isinstance(board_mas[self.x][self.y - 1], Point):
                moves.append([self.x, self.y - 1])

        return moves
