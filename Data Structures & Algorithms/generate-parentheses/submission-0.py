class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_cnt, close_cnt):
            if open_cnt == close_cnt == n:
                res.append("".join(stack))

            if open_cnt < n:
                stack.append("(")
                backtrack(open_cnt + 1, close_cnt)
                stack.pop()
            if close_cnt < open_cnt:
                stack.append(")")
                backtrack(open_cnt, close_cnt + 1)
                stack.pop()

        backtrack(0, 0)
        return res