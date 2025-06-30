import random

class RandomAI:
    def init(self, board):
        self.board = board

    def get_random_move(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                square = self.board.squares[row][col]
                if square.has_piece() and square.piece.color == color:
                    self.board.calc_moves(square.piece, row, col)
                    for move in square.piece.moves:
                        moves.append((square.piece, move))
        if moves:
            return random.choice(moves)
        return None, None
