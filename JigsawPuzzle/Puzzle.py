class Singleton(type):
    __instances = None

    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances

class Puzzle(metaclass=Singleton):
    def __init__(self):
        self.__board = [[None for _ in range(3)] for _ in range(3)]
        self.__free = [] 

    def insert_piece(self, piece, row, column):
        if 0 <= row < len(self.__board) and 0 <= column < len(self.__board[0]):
            if self.__board[row][column] is None:  
                self.__board[row][column] = piece
                return True
            else:
                print(f"Position ({row}, {column}) is already occupied.")
                return False
        else:
            print(f"Position ({row}, {column}) is out of bounds.")
            return False

    def display_board(self):
        for row in self.__board:
            print(row)

# Example usage:
puzzle = Puzzle()
puzzle.insert_piece('X', 0, 0)
puzzle.display_board()

#Here the puzzle will use the singleton design pattern
