import numpy as np
from const import *


class Board: 
    def __init__(self):
        self.squares = np.zeros((ROW,COLS))
        print(self.squares) ## Only a test print  
        
        
    def chose_a_square(self,row,col,player): 
        self.squares[row][col] = player
    
    
    ## Check if a square is empty
    def avilable_square(self,row,col): 
        if self.squares[row][col] == 0: 
            return True
        else: 
            return False