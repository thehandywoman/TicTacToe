import pygame
import sys
from Board import Board
from Player import Player
from GameLogic import GameLogic

class Main:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 300
        self.SCREEN_HEIGHT = 400
        self.LINE_COLOR = (0, 0, 0)
        self.BG_COLOR = (255, 255, 255)
        self.LINE_WIDTH = 4
        self.BOARD_SIZE = 3
        self.INFO_SPACE_HEIGHT = 50
        self.INFO_COLOR = (100, 100, 100)
        self.TEXT_COLOR = (255, 255, 255)
        self.CROSS_COLOR = (255, 0, 0)
        self.CIRCLE_COLOR = (0, 0, 255)
        self.BUTTON_COLOR = (100, 100, 100)
        self.BUTTON_TEXT_COLOR = (255, 255, 255)
        self.font = pygame.font.Font(None, 24)

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")

        self.board = Board(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.BOARD_SIZE,
                           self.INFO_SPACE_HEIGHT, self.LINE_COLOR, self.LINE_WIDTH)
        self.player = Player('X')
        self.computer = Player('O')
        self.game_logic = GameLogic(self.board, self.player, self.computer)
        self.info_space = self.board.info_space

        self.reset_button = pygame.Rect(20, self.SCREEN_HEIGHT - self.INFO_SPACE_HEIGHT + 10, 260, 30)


    def draw(self):
        self.screen.fill(self.BG_COLOR)
        self.board.draw(self.screen)

        pygame.draw.rect(self.screen, self.INFO_COLOR, self.info_space)
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, self.reset_button)
        reset_text = self.font.render("Once more", True, self.BUTTON_TEXT_COLOR)
        reset_text_rect = reset_text.get_rect(center=self.reset_button.center)
        self.screen.blit(reset_text, reset_text_rect)

        if self.game_logic.game_over:
            winner = self.board.check_winner()
            if winner:
                message = f"Player {winner} wins!" if winner == 'X' else f"Computer {winner} wins!"
            else:
                message = "It's a tie!"
            text = self.font.render(message, True, self.TEXT_COLOR)
            text_rect = text.get_rect(center=(self.SCREEN_WIDTH // 2, self.INFO_SPACE_HEIGHT // 2))
            self.screen.blit(text, text_rect)

        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                symbol = self.board.board[row][col]
                if symbol != ' ':
                    font = pygame.font.Font(None, 100)
                    color = self.CROSS_COLOR if symbol == 'X' else self.CIRCLE_COLOR
                    text = font.render(symbol, True, color)
                    text_rect = text.get_rect(center=(
                    col * self.board.SQUARE_SIZE + self.board.SQUARE_SIZE // 2,
                    self.INFO_SPACE_HEIGHT + row * self.board.SQUARE_SIZE + self.board.SQUARE_SIZE // 2))
                    self.screen.blit(text, text_rect)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_logic.game_over:
            self.game_logic.handle_event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.game_logic.game_over:
            if self.reset_button.collidepoint(event.pos):
                self.board.reset()
                self.game_logic.game_over = False
                self.game_logic.current_player = self.player

    def run(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.handle_event(event)

if __name__ == "__main__":
    main = Main()
    main.run()