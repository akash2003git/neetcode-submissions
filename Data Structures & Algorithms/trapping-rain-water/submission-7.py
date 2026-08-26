class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0 for i in range(n)]
        maxRight = [0 for i in range(n)]
        res = 0

        # Compute maxLeft
        maxL = height[0]
        for i in range(1, n, 1):
            maxLeft[i] = maxL
            maxL = max(height[i], maxL)
        
        # Compute maxRight
        maxR = height[n-1]
        for i in range(n - 1, -1, -1):
            maxRight[i] = maxR
            maxR = max(height[i], maxR)

        for i in range(n):
            waterLvl = min(maxLeft[i], maxRight[i]) - height[i]
            if waterLvl > 0:
                res += waterLvl
            
        return res
            