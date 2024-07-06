import pygame
import sys
from const import *
from ai import AI
from board import Board

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('TIC TAC TOE AI')
        self.screen.fill(BG_COLOR)
        
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.gamemode = 'ai'
        self.running = True
        self.show_lines()

    def show_lines(self):
        self.screen.fill(BG_COLOR)
        for i in range(1, COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQSIZE, 0), (i * SQSIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQSIZE), (WIDTH, i * SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            
            ## Drawing the circle first
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(self.screen, green_color, center, CIRCLE_RADIUS, CIRCLE_WIDTH)
            
        # the x
        elif self.player == 2:
            start_desc = (col * SQSIZE + SPACE, row * SQSIZE + SQSIZE - SPACE)
            end_desc = (col * SQSIZE + SQSIZE - SPACE, row * SQSIZE + SPACE)
            start_asc = (col * SQSIZE + SPACE, row * SQSIZE + SPACE)
            end_asc = (col * SQSIZE + SQSIZE - SPACE, row * SQSIZE + SQSIZE - SPACE)
            pygame.draw.line(self.screen, CROSS_LINE_COLOR, start_desc, end_desc, LINE_WIDHT_CROSS)
            pygame.draw.line(self.screen, CROSS_LINE_COLOR, start_asc, end_asc, LINE_WIDHT_CROSS)

    def make_move(self, row, col):
        self.board.chose_a_square(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def isover(self):
        return self.board.final_state() != 0 or self.board.board_full()


    ## Reset function when the game is done by pressing r.
    def reset(self):
        self.__init__()

def main():
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if game.board.empty_square(row, col) and game.running:
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    game.change_gamemode()

                if event.key == pygame.K_r:
                    game.reset()

        if game.gamemode == 'ai' and game.player == game.ai.player and game.running:
            row, col = game.ai.evaluate(game.board)
            game.make_move(row, col)

            if game.isover():
                game.running = False

        pygame.display.update()



main()
