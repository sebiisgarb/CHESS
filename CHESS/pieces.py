class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_valid_moves(self, board):
        pass


class Pawn(Piece):
    super().__init__(Piece)

    def get_valid_moves(self, board):
        self.position