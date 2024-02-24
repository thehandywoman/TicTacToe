import random
import pygame

class GameLogic:
    def __init__(self, board, player, computer):
        self.board = board
        self.player = player
        self.computer = computer
        self.current_player = self.player
        self.game_over = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            x, y = pygame.mouse.get_pos()
            row = (y - self.board.INFO_SPACE_HEIGHT) // self.board.SQUARE_SIZE
            col = x // self.board.SQUARE_SIZE
            if self.board.mark_square(row, col, self.player.symbol):
                winner = self.board.check_winner()
                if winner:
                    self.game_over = True
                elif self.board.is_full():
                    self.game_over = True
                else:
                    self.current_player = self.computer
                    self.computer_move()

                if not self.game_over:
                    computer_winner = self.board.check_winner()
                    if computer_winner:
                        self.game_over = True

        elif event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
            if self.reset_button.collidepoint(event.pos):
                self.board.reset()
                self.game_over = False
                self.current_player = self.player

    def computer_move(self):
        for row in range(self.board.BOARD_SIZE):
            for col in range(self.board.BOARD_SIZE):
                if self.board.board[row][col] == ' ':
                    self.board.board[row][col] = self.player.symbol
                    if self.board.check_winner() == self.player.symbol:
                        self.board.board[row][col] = self.computer.symbol
                        return
                    else:
                        self.board.board[row][col] = ' '

        for row in range(self.board.BOARD_SIZE):
            for col in range(self.board.BOARD_SIZE):
                if self.board.board[row][col] == ' ':
                    self.board.board[row][col] = self.computer.symbol
                    if self.board.check_winner() == self.computer.symbol:
                        self.game_over = True
                        return
                    else:
                        self.board.board[row][col] = ' '

        available_squares = [(row, col) for row in range(self.board.BOARD_SIZE) for col in range(self.board.BOARD_SIZE) if
                             self.board.board[row][col] == ' ']
        if available_squares:
            row, col = random.choice(available_squares)
            self.board.mark_square(row, col, self.computer.symbol)

            winner = self.board.check_winner()
            if winner:
                self.game_over = True
            elif self.board.is_full():
                self.game_over = True
