class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Check if triplets are even possible
            if a > 0:
                break
            
            # Skip duplicates
            if i >0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Optionally skipping from right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
                    
            
        return res