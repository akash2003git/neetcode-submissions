class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []

        def backtrack(i, remaining):
            if remaining < 0 or i > len(nums) - 1:
                return
            elif remaining == 0:
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            backtrack(i, remaining - nums[i])
            subSet.pop()
            backtrack(i + 1, remaining)

        backtrack(0, target)
        return res