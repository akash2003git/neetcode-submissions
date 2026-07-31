class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num
        
        res = [0] * len(nums)
        if zero_cnt > 1:
            return res

        for i, num in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num
        
        return res