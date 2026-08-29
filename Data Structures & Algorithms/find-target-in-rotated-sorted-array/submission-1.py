class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        miniIdx = 0

        while l <= r:
            if nums[l] <= nums[r]:
                miniIdx = l
                break
            
            m = (l + r) // 2

            if nums[m] >= nums[l]:
                l = m + 1
                miniIdx = l
            else:
                r = m
                miniIdx = m
                
        if target <= nums[len(nums) - 1]:
            l, r = miniIdx, len(nums) - 1
        else:
            l, r = 0, miniIdx - 1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m                

        return -1