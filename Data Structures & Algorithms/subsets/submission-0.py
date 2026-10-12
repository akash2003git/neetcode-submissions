class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, subSets = [], []
        self.helper(0, nums, curSet, subSets)
        return subSets

    def helper(self, i, nums, curSet, subSets):
        if i >= len(nums):
            subSets.append(curSet.copy())
            return

        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, subSets)

        curSet.pop()
        self.helper(i + 1, nums, curSet, subSets)