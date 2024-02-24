import pygame

class Board:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_SIZE, INFO_SPACE_HEIGHT, LINE_COLOR, LINE_WIDTH):
        self.board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.SQUARE_SIZE = min(SCREEN_WIDTH // BOARD_SIZE, (SCREEN_HEIGHT + INFO_SPACE_HEIGHT) // BOARD_SIZE)
        self.INFO_SPACE_HEIGHT = INFO_SPACE_HEIGHT
        self.LINE_COLOR = LINE_COLOR
        self.LINE_WIDTH = LINE_WIDTH
        self.info_space = pygame.Rect(0, 0, SCREEN_WIDTH, INFO_SPACE_HEIGHT)
        self.BOARD_SIZE = BOARD_SIZE

    def draw(self, screen):
        for i in range(len(self.board)):
            pygame.draw.line(screen, self.LINE_COLOR, (0, self.INFO_SPACE_HEIGHT + i * self.SQUARE_SIZE),
                             (len(self.board) * self.SQUARE_SIZE, self.INFO_SPACE_HEIGHT + i * self.SQUARE_SIZE),
                             self.LINE_WIDTH)
            pygame.draw.line(screen, self.LINE_COLOR, (i * self.SQUARE_SIZE, self.INFO_SPACE_HEIGHT),
                             (i * self.SQUARE_SIZE, len(self.board) * self.SQUARE_SIZE + self.INFO_SPACE_HEIGHT), self.LINE_WIDTH)


    def mark_square(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        return False

    def check_winner(self):
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_full(self):
        for row in self.board:
            for square in row:
                if square == ' ':
                    return False
        return True

    def reset(self):
        self.board = [[' ' for _ in range(len(self.board))] for _ in range(len(self.board))]
