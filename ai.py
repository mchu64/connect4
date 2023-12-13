#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from methods import *
from board import Board
from player import Player

class AIPlayer(Player):
    'A subclass of Player that uses AI techniques to choose moves'
    def __init__(self, checker, tiebreak, lookahead):
        "A constructor for this class taking in checker, tiebreak, lookahead"
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        'returns the checker, what type of tiebreak, and lookahead'
        return 'Player' + ' ' + str(self.checker) + ' ' + '(' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        'Returns the highets column score'
        max_scores = []
        for x in range(len(scores)):
            if scores[x] == max(scores):
                max_scores += [x]
        if self.tiebreak == 'LEFT':
            return min(max_scores)
        if self.tiebreak == 'RIGHT':
            return max(max_scores)
        if self.tiebreak == 'RANDOM':
            return random.choice(max_scores)
        
    def scores_for(self, b):
        'Creates column score list for the input board'
        score = [50] * b.width
        for x in range(b.width):
            if b.can_add_to(x) == False:
                score[x] = -1
            elif b.is_win_for(self.checker) == True:
                score[x] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                score[x] = 0
            elif self.lookahead == 0:
                score[x] = 50
            else:
                b.add_checker(self.checker, x)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(b)
                if max(opp_scores) == 100:
                    score[x] = 0
                if max(opp_scores) == 0:
                    score[x] = 100
                if max(opp_scores) == 50:
                    score[x] = 50
                b.remove_checker(x)
        return score
        
    
    def next_move(self, b):
        'return the called AIPlayer‘s judgment of its best possible move'
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
            
            
            
            
            
            
            
            
            
            