class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        # Check all columns
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        # Check all nine 3x3 squares
        for square in range(9):
            seen = set()
            for i in range(3):
                row = (square // 3) * 3 + i
                for j in range(3):
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True