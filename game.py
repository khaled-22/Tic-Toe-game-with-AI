from const import * 
from main import *
import pygame

class Game: 
    def __init__(self):
        self.show_lines()

    def show_lines(self): 
        # Vertical lines 
        pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HEIGHT),LINE_WIDTH)
        
        ## Horizontal lines 
        pygame.draw.line(screen,LINE_COLOR,(0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)