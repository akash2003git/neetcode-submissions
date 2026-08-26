class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        l, r = 0, n - 1 
        leftMax, rightMax = height[0], height[n - 1]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res