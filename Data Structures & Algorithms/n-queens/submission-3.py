class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = []
        cols = set()
        neg_diag = set()   # r - c
        pos_diag = set()   # r + c

        def backtrack(row):
            if row >= n:
                res.append(queens.copy())
                return

            for col in range(n):

                if (col not in cols and
                    row-col not in neg_diag and
                    row+col not in pos_diag):

                    queen_str = "." * col + "Q" + "." * (n - col - 1)
                    queens.append(queen_str)
                    cols.add(col)
                    neg_diag.add(row-col)
                    pos_diag.add(row+col)
                    backtrack(row + 1)
                    queens.pop()
                    cols.remove(col)
                    neg_diag.remove(row-col)
                    pos_diag.remove(row+col)

        backtrack(0)

        # Convert coordinates into board representation
        # for sol in res_cords:
        #     board = []
        #     for (r, c) in sol:
        #         queen_str = ""
        #         for i in range(n):
        #             if i == c:
        #                 queen_str += "Q"
        #             else:
        #                 queen_str += "."
        #         board.append(queen_str)
        #     res.append(board)

        return res

    # def isValid(self, row, col, queens):
    #     for (r, c) in queens:
    #         if col == c or abs(row - r) == abs(col - c):
    #             return False
    #     return True