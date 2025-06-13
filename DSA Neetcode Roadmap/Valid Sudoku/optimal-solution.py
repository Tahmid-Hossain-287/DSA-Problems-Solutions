class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        box = {}

        for r in board:
            for c in r:
                if (board[r][c] in row[r] or
                board[r][c] in column[c] or
                board[r][c] in box[(row //3, column //3)]):
                    return False
                
                row[r].append(board[r][c])
                column[c].append(board[r][c])
                box[(row // 3, column // 3)].append(board[r][c])

        return True