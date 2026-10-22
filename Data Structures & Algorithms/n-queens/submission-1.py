class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res_cords = []
        res = []
        queens = []

        def backtrack(row):
            if row >= n:
                res_cords.append(queens.copy())
                return

            for col in range(n):
                if self.isValid(row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1)
                    queens.pop()

        backtrack(0)

        # Convert coordinates into board representation
        for sol in res_cords:
            board = []
            for (r, c) in sol:
                queen_str = ""
                for i in range(n):
                    if i == c:
                        queen_str += "Q"
                    else:
                        queen_str += "."
                board.append(queen_str)
            res.append(board)
        return res

    def isValid(self, row, col, queens):
        for (r, c) in queens:
            if col == c or abs(row - r) == abs(col - c):
                return False
        return True