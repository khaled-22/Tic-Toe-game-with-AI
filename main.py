import numpy as np
import pygame 
import sys 
from const import * 
from board import Board
## 

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-Toe")
screen.fill(BG_COLOR)


class Game: 
    def __init__(self):
        self.show_lines()
        self.player = 1
        self.board = Board()


    ## Draw the lines 
    def show_lines(self): 
        # Vertical lines 
        pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HEIGHT),LINE_WIDTH)
        
        ## Horizontal lines 
        pygame.draw.line(screen,LINE_COLOR,(0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(0,HEIGHT-SQSIZE),(WIDTH,HEIGHT-SQSIZE),LINE_WIDTH)


    def next_turn(self): 
        self.player = self.player % 2 + 1        

    def draw_fig(self,row,col):
        ## First player will draw circle first
        ## start_dsc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
        if self.player == 1: 
            pygame.draw.circle(screen,GREEN,(int(col * 200 + 200 /2),int (row * 200 + 200 / 2)),CIRCLE_RADIUS,CIRCLE_WIDTH)            
        # draw cross 
        elif self.player == 2: 
            pygame.draw.line(screen,CROSS_LINE_COLOR,(col * 200 + SPACE ,row * 200 + 200 - SPACE),(col * 200 + 200 -SPACE, row * 200 + SPACE),LINE_WIDHT_CROSS)
            pygame.draw.line(screen,CROSS_LINE_COLOR,(col * 200 + SPACE ,row * 200 + SPACE),(col * 200 + 200 -SPACE, row * 200 + 200 - SPACE),LINE_WIDHT_CROSS)
        
def main():    
    game = Game()
    board = game.board
    
    ## Main-loop
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN: 
                print(event.pos) ## Printing the coordiantes for mouse click 
                
                pos = event.pos 
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                print(row,col) ## 
                
                if board.avilable_square(row,col):
                    board.chose_a_square(row,col,1)
                    game.draw_fig(row,col)
                    game.next_turn()
                    print(board.squares)
        
    
    
    
        pygame.display.update()
main()