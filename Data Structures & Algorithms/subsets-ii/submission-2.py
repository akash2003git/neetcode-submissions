class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_set = []
        nums.sort()

        def backtrack(i):
            if i > len(nums) - 1:
                res.append(sub_set.copy())
                return

            sub_set.append(nums[i])
            backtrack(i + 1)

            sub_set.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res