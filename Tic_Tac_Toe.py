class Board:
    
    # Define the __init__ method to set the dimension of the board and the symbols 'X' and 'O' that will be used to play the game
    def __init__(self, board_dimension='3x3'):
        # Set the default argument to avoid argument messing error
        self.board = []
        self.board_row = 3
        self.board_column = 3

        # Define the symbols 'X' and 'O'
        self.PLAYER_X_SYMBOL = 'X'
        self.PLAYER_O_SYMBOL = 'O'

        # set the dimension of the board
        try:
            # Check if the board_dimension value is in the format of 'NxM'
            if board_dimension.count('x') == 1:
                # Split the board_dimension value to two part the row part and the column part
                board_dimension = board_dimension.split('x')
                
                # Check if the row part and the column part are integers
                if board_dimension[0].isdigit() and board_dimension[1].isdigit():
                    # Set the value of the number of rows and columns
                    row, column = map(int, board_dimension)

                    # Chech if the number of rows and column is between the max and the min
                    if not (3 <= row <= 10 and 3 <= column <= 10):
                        raise ValueError('Invalid input: Board dimensions must be between 3x3 and 10x10')
                    self.board_row = row
                    self.board_column = column
                else:
                    raise ValueError("Invalid input: Board dimensions must be integers")
            else:
                raise ValueError("Invalid input: Board dimensions must be in the format 'NxM'")
        except ValueError as e:
            print(e)

    
    # Define the __str__ method to create the board where to play
    def __str__(self):
        self.board = []
        
        # Create the varibales which will contain the vertical and the horizental lines
        vertical_line = f'{"   |" * (self.board_column - 1) }   '
        horizontal_line = f'{"───┼" * (self.board_column - 1)}───'

        # Create the board
        self.board.append(vertical_line)
        for i in range(1, self.board_row * 2):
            if i % 2 == 0:
                self.board.append(horizontal_line)
            else:
                self.board.append(vertical_line)
        self.board.append(vertical_line)
        
        # Return the board
        return '\n'.join(self.board)
        

    # Helper method to validate row input
    def _is_valid_row(self, row):
        return isinstance(row, int) and 1 <= row <= self.board_row
    

    # Helper method to validate column input
    def _is_valid_column(self, column):
        return isinstance(column, int) and 1 <= column <= self.board_column


    # Define the place method to place the user symbol in the specific case
    def place(self, symbol, row, column):

        # Validate row input
        if not self._is_valid_row(row):
            raise ValueError("Invalid row input: Row must be an integer between 1 and the number of rows on the board.")

        # Validate column input
        if not self._is_valid_column(column):
            raise ValueError("Invalid column input: Column must be an integer between 1 and the number of columns on the board.")
        
        try:
            # Assign the original values of both row and column to evade error indexing
            row = row * 2 - 1
            column = column * 4 - 3
                
            # Check if the defined position is occupied
            if self.board[row][column] == ' ' and self.board[row][column] not in ['X', 'O']:
                    
                # Replace the space by the symbol
                converted_row = list(self.board[row])
                converted_row[column] = symbol
                self.board[row] = ''.join(converted_row)
                        
                # Return the result
                return '\n'.join(self.board)
            else:
                return f'Error: The position selected contain already {self.board[row][column]}'
        except ValueError as e:
            return e      

    
    # Define a method that check if 'X' or 'O' is verticaly aligned
    def check_column(self, symbol):
        for column in range(1, self.board_column * 4 - 1, 4):
            if all(self.board[row][column] == symbol for row in range(1, self.board_row * 2, 2)):
                return True
        return False

    
    # Define a method that check if 'X' or 'O' is horizontaly alinged  
    def check_row(self, symbol):
        for row in range(1, self.board_row * 2, 2):
            if all(self.board[row][column] == symbol for column in range(1, self.board_column * 4 - 1, 4)):
                return True
        return False
        
        
    # Define a method that check if 'X' or 'O' is diagonaly aligned
    def check_diagonal(self, symbol):
        return all(
            self.board[row][row * 2 - 1] == symbol for row in range(1, self.board_row * 2, 2)
        ) or all(
            self.board[row][self.board_column * 4 - 2 * row - 1] == symbol for row in range(1, self.board_row * 2, 2)
        )


    # Define a method that return a message if the player won the game
    def check_win(self, symbol):
        if self.check_row(symbol) or self.check_column(symbol) or self.check_diagonal(symbol):
            return f'The player \'{symbol}\' won the game'
        
    
    # Define a method that test the overall class methods
    def test(self):
        board = Board()
        # test the row win condition
        print('Let play:\n')
        print(board, '\n')
        print(board.place('X', 1, 1), '\n')
        print(board.place('O', 1, 1), '\n')
        print(board.place('X', 1, 2), '\n')
        print(board.place('X', 1, 3), '\n')
        print(board.check_win('X'))
        # test the column win condition
        print('Let play:\n')
        print(board)
        print(board.place('O', 1, 1), '\n')
        print(board.place('O', 2, 1), '\n')
        print(board.place('O', 3, 1), '\n')
        print(board.check_win('O'))
        
        # test the diagonal win condition
        print('Let play:\n')
        print(board, '\n')
        print(board.place('O', 1, 1), '\n')
        print(board.place('O', 2, 2), '\n')
        print(board.place('O', 3, 3), '\n')
        print(board.check_win('O'))
        

# Test the project
Board().test()
