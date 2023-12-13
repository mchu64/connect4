#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    
    def __init__(self, height, width):
        "constructs a new Board object that has height and width"
        
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###  
        for x in range((self.width*2)+1):
            s += '-'
        s += '\n'
        
        for x in range(self.width):
            s += ' ' + str(x%10)
        s += '\n'
        
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        for row in range(self.height):
            if self.slots[row][col] == ' ':
                x = row

        self.slots[x][col] = checker
    ### add your reset method here ###
    
    def reset(self):
        'resets board'
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
                
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    def can_add_to(self, col):
        'checks if the column can be added to'
        if col not in range(self.width):
            return False
        for x in range(self.height):
                if self.slots[x][col] == ' ':
                    return True
        return False
    
    def is_full(self):
        'checks to see if board is full'
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        else:
            return True
        
    def remove_checker(self, col):
        'removes checker'
        for row in range(self.height):
            if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                self.slots[row][col] = ' '
                break
            
            
    def is_horizontal_win(self, checker):
        'Checks for a horizontal win for the specified checker.'
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
               self.slots[row][col + 1] == checker and \
               self.slots[row][col + 2] == checker and \
               self.slots[row][col + 3] == checker:
                   return True
               
     # if we make it here, there were no horizontal wins
        return False
            
    def is_vertical_win(self, checker):
        'checks for a vertical win'
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                     return True
        return False
                            
    def is_down_diagonal_win(self, checker):
        'checks for a win going from down, left to right'
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                     return True
        return False
                 
    def is_up_diagonal_win(self, checker):
        'checks for a win that goes up from left to right'
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                     return True
        return False
        



    def is_win_for(self, checker):
        'checks for 4 in a row in any orientation'
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
            self.is_vertical_win(checker) == True or \
                self.is_down_diagonal_win(checker) == True or \
                    self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
        
        
        
        
        
