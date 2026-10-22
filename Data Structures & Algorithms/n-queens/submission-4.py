class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []

        used_cols = set()
        used_neg_diagonals = set()  # row - col
        used_pos_diagonals = set()  # row + col

        def backtrack(row):
            if row == n:
                result.append(board.copy())
                return

            for col in range(n):
                neg_diagonal = row - col
                pos_diagonal = row + col

                if (
                    col in used_cols
                    or neg_diagonal in used_neg_diagonals
                    or pos_diagonal in used_pos_diagonals
                ):
                    continue

                # Choose
                row_string = "." * col + "Q" + "." * (n - col - 1)
                board.append(row_string)
                used_cols.add(col)
                used_neg_diagonals.add(neg_diagonal)
                used_pos_diagonals.add(pos_diagonal)

                # Explore
                backtrack(row + 1)

                # Unchoose
                board.pop()
                used_cols.remove(col)
                used_neg_diagonals.remove(neg_diagonal)
                used_pos_diagonals.remove(pos_diagonal)

        backtrack(0)
        return result