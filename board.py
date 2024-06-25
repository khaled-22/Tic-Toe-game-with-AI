import numpy as np
from const import *

class Board: 
    def __init__(self):
        self.squares = np.zeros((ROW, COLS))
        self.marked_squares = 0

    def final_state(self):
        for col in range(COLS): 
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0: 
                return self.squares[0][col]
            
        for row in range(ROW): 
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0: 
                return self.squares[row][0]
            
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0: 
            return self.squares[1][1]

        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0: 
            return self.squares[1][1]
                
        return 0
        
    def chose_a_square(self, row, col, player): 
        self.squares[row][col] = player
        self.marked_squares += 1 
    
    def empty_square(self, row, col): 
        return self.squares[row][col] == 0

    
    def get_empty_squares(self): 
        empty_squares = []
        for row in range(ROW):
            for col in range(COLS): 
                if self.empty_square(row, col):
                    empty_squares.append((row, col))
        return empty_squares
    
    
    
    def board_full(self):
        return self.marked_squares == 9
    
    def available_square(self, row, col): 
        return self.squares[row][col] == 0
