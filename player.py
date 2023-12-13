#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from board import Board

# write your class below.

class Player:
    'player for the connect 4 game'
    def __init__(self, checker):
        'constructs a player object that has '
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        'Returns a string of the player name'
        return 'Player' + ' ' + str(self.checker)
    
    
    def opponent_checker(self):
        'returns the opponent checker'
        if self.checker == 'X':
            opponent = 'O'
        else:
            opponent = 'X'
            
        return opponent
    
    def next_move(self, b):
        'Takes a board as an input and sees if the column can have a move take place'
        self.num_moves += 1
        loop = True
        while loop == True:
            x = int(input('Enter a column: '))
            if x in range(b.width):
                break
            else:
                print('Try Again!')
                print('')
        return x
    
    
    