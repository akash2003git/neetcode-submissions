class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            # left portion is sorted
            # i.e. 1 possibility in sorted portion (left)
            # and 2 possibility in unsorted portion (right)
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
            # right portion is sorted
            # i.e. 2 possibility in unsorted portion (left)
            # and 1 possibility in sorted portion (right)
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1