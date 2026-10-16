class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []

        def backtrack(i):
            total = sum(subSet)
            rem = target - total
            if rem < 0 or i > len(nums) - 1:
                return
            elif rem == 0:
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            backtrack(i)
            subSet.pop()
            backtrack(i + 1)

        backtrack(0)
        return res