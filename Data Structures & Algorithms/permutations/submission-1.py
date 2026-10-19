class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in nums:
                if n not in perm:
                    perm.append(n)
                    backtrack()
                    perm.pop()

        backtrack()
        return res