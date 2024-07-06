import random
import math 
import copy


class AI: 
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player 
    
    
    def random_choice(self, board):
        empty_sqrs = board.get_empty_squares()
        index = random.randrange(0, len(empty_sqrs))


        return empty_sqrs[index] 
    
    
    def minimax(self,board,maximizing_player): 
        # 1. check the terminal cases 
        case = board.final_state()
        
        if case == 1:
            return 1, None
        if case == 2:
            return -1, None
        if board.board_full():
            return 0, None
        

        # if maximizing player, get the max value 
        if maximizing_player: 
            max_eval = -math.inf
            best_move = None
            empty_sqrs = board.get_empty_squares()

            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.chose_a_square(row,col,1)
                eval = self.minimax(temp_board,False)[0]
                
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
            return max_eval, best_move
        
        
        
        elif not maximizing_player:
            min_eval = math.inf
            best_move = None
            empty_sqrs = board.get_empty_squares()
            
            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.chose_a_square(row,col,self.player)
                eval = self.minimax(temp_board,True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
            
            return min_eval, best_move


    def evaluate(self, main_board):
        if self.level == 0:
            eval = 'random'
            move = self.random_choice(main_board)

        else:
            eval, move = self.minimax(main_board, False)
   
        
        print(f'AI Move: {move} with an evaluation of {eval}')
        
        return move  # Always return (row, col) tuple
