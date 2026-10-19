class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_set = []

        def backtrack(i):
            if i >= len(nums):
                res.append(sub_set.copy())
                return

            sub_set.append(nums[i])
            backtrack(i + 1)

            sub_set.pop()
            backtrack(i + 1)

        backtrack(0)
        return res