class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in board:
            row = [num for num in i if num != '.']
            if len(row) != len(set(row)):
                return False
        
        # Check columns
        col_length = len(board[0])
        row_length = len(board)

        for j in range(col_length):
            col = []
            for i in range(row_length):
                if board[i][j] != '.':
                    col.append(board[i][j])
            if len(col) != len(set(col)):
                return False
        
        return True


// row and column check done. now only 3X3 box check is left