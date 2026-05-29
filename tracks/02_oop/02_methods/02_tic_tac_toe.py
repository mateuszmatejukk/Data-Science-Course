class TicTacToe:
    """
    >>> game = TicTacToe(board_size=2)
    >>> game.print_board()
    .AB
    1..
    2..
    >>> game = TicTacToe(board_size=3)
    >>> game.print_board()
    .ABC
    1...
    2...
    3...

    >>> game = TicTacToe(board_size=3)
    >>> game.move(row=0, col=1, player='X')
    >>> game.print_board()
    .ABC
    1.X.
    2...
    3...


    >>> game = TicTacToe(board_size=3)
    >>> game.move(row=0, col=0, player='X')
    >>> game.print_board()
    .ABC
    1X..
    2...
    3...

    >>> game = TicTacToe(board_size=2)
    >>> game.move(row=1, col=1, player='O')
    >>> game.print_board()
    .AB
    1..
    2.O


    >>> game = TicTacToe(board_size=3)
    >>> game.move(row=0, col=0, player='X')
    >>> game.move(row=0, col=0, player='O')
    Traceback (most recent call last):
    ...
    ValueError: To pole jest już zajęte
    """

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [['.'] * board_size for _ in range(board_size)]
        # self.board = [['.'] * board_size] * board_size

    def print_board(self):
        letters = 'ABCDEFGHIJKLMNOPRS'
        print('.' + letters[:self.board_size])
        for index in range(self.board_size):
            # print(f"{index + 1}{self.board[index]}")
            row = ''.join(self.board[index])
            print(f"{index + 1}{row}")

    def move(self, row, col, player):
        # self.board[row][col] = player
        if self.board[row][col] != '.':
            raise ValueError('To pole jest już zajęte')

        self.board[row][col] = player


if __name__ == '__main__':

    game = TicTacToe(board_size=3)
    game.move(row=0, col=0, player='X')
    game.print_board()
